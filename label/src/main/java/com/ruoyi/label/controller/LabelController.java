package com.ruoyi.label.controller;

import java.util.*;
import javax.servlet.http.HttpServletResponse;

import com.ruoyi.label.controller.vo.LabelQuery;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.ruoyi.common.annotation.Log;
import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.domain.AjaxResult;
import com.ruoyi.common.enums.BusinessType;
import com.ruoyi.label.domain.Label;
import com.ruoyi.label.service.ILabelService;
import com.ruoyi.common.utils.poi.ExcelUtil;

/**
 * 标签系统Controller
 * 
 * @author ZeyuZuo
 * @date 2024-07-24
 */
@RestController
@RequestMapping("/system/label")
public class LabelController extends BaseController
{
    @Autowired
    private ILabelService labelService;

    /**
     * 查询父节点的子节点
     */
    @GetMapping("/children/{parentName}")
    public AjaxResult children(@PathVariable("parentName") String parentName)
    {
        Label tmp = new Label();
        tmp.setName(parentName);
        List<Label> labels = labelService.selectLabelList(tmp);
        tmp.setName(null);

        List<Label> list = new ArrayList<>();

        for(Label label : labels) {
            list.add(label);
            tmp.setParentId(label.getId());
            list.addAll(labelService.selectLabelList(tmp));
        }

        // List<Label> list = labelService.selectLabelList(new Label());
        return success(list);
    }

    /**
     * 查询标签系统列表
     */
    @PreAuthorize("@ss.hasPermi('system:label:list')")
    @GetMapping("/list")
    public AjaxResult list(LabelQuery query)
    {
        System.out.println(query);

//        // 如果没有查询条件，返回所有标签
//        if(Objects.isNull(query.getName()) && Objects.isNull(query.getParentName())) {
//            return success(labelService.selectLabelList(new Label()));
//        }

        Label tmp = new Label();

        if(Objects.isNull(query.getName()) && Objects.isNull(query.getParentName())) {
            return success(labelService.selectLabelList(new Label()));
        } else if (!Objects.isNull(query.getName()) && !Objects.isNull(query.getParentName())) {
            tmp.setName(query.getName());
            List<Label> labels = labelService.selectLabelList(tmp);
            tmp.setName(null);

            Set<Label> list = new HashSet<>();
            for(Label label : labels) {
                if(label.getParentId() != null) {
                    Label parent = labelService.selectLabelById(label.getParentId());
                    if(!Objects.isNull(parent) && parent.getName().contains(query.getParentName())) {
                        list.add(label);
                        list.add(parent);
                        list.addAll(getAllChildren(label));
                    }
                }
            }

            return success(list);
        } else {
            String name = "";
            if(!Objects.isNull(query.getName())){
                name = query.getName();
            } else {
                name = query.getParentName();
            }
            tmp.setName(name);
            List<Label> labels = labelService.selectLabelList(tmp);
            tmp.setName(null);

            Set<Label> list = new HashSet<>();
            for(Label label : labels) {
                list.add(label);
                list.addAll(getAllChildren(label));
            }

            return success(list);
        }

//        if(!Objects.isNull(query.getName())) {
//            if(!Objects.isNull(query.getParentName())) {
//                /*
//                 * 先根据name查询标签，再判断它的parentName是否是query.getParentName()，都是模糊查询
//                 */
//                tmp.setName(query.getName());
//                List<Label> labels = labelService.selectLabelList(tmp);
//                tmp.setName(null);
//
//                Set<Label> list = new HashSet<>();
//                for(Label label : labels) {
//                    if(label.getParentId() != null) {
//                        Label parent = labelService.selectLabelById(label.getParentId());
//                        if(!Objects.isNull(parent) && parent.getName().contains(query.getParentName())) {
//                            list.add(label);
//                            list.add(parent);
//                            list.addAll(getAllChildren(label));
//                        }
//                    }
//                }
//
//                return success(list);
//            } else {
//                tmp.setName(query.getName());
//                List<Label> labels = labelService.selectLabelList(tmp);
//                tmp.setName(null);
//
//                Set<Label> list = new HashSet<>();
//                for(Label label : labels) {
//                    list.add(label);
//                    list.addAll(getAllChildren(label));
//                }
//
//                return success(list);
//            }
//        } else {
//            if(Objects.isNull(query.getParentName())) {
//                return success(labelService.selectLabelList(new Label()));
//            } else {
//                tmp.setName(query.getParentName());
//                List<Label> labels = labelService.selectLabelList(tmp);
//                tmp.setName(null);
//
//                Set<Label> list = new HashSet<>();
//                for(Label label : labels) {
//                    list.add(label);
//                    list.addAll(getAllChildren(label));
//                }
//
//                return success(list);
//            }
//        }

    }

    private List<Label> getAllChildren(Label parentLabel) {
        List<Label> allChildren = new ArrayList<>();
        Label tmp = new Label();
        tmp.setParentId(parentLabel.getId());
        List<Label> directChildren = labelService.selectLabelList(tmp);

        for (Label child : directChildren) {
            allChildren.add(child);
            allChildren.addAll(getAllChildren(child)); // 递归获取子节点的子节点
        }

        return allChildren;
    }

    private Label getParent(Label label) {
        Label parent = labelService.selectLabelById(label.getParentId());
        if(parent == null) {
            return label;
        }
        return parent;
    }

    /**
     * 导出标签系统列表
     */
    @PreAuthorize("@ss.hasPermi('system:label:export')")
    @Log(title = "标签系统", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, Label label)
    {
        List<Label> list = labelService.selectLabelList(label);
        ExcelUtil<Label> util = new ExcelUtil<>(Label.class);
        util.exportExcel(response, list, "标签系统数据");
    }

    /**
     * 获取标签系统详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:label:query')")
    @GetMapping(value = "/{id}")
    public AjaxResult getInfo(@PathVariable("id") Long id)
    {
        return success(labelService.selectLabelById(id));
    }

    /**
     * 新增标签系统
     */
    @PreAuthorize("@ss.hasPermi('system:label:add')")
    @Log(title = "标签系统", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody Label label)
    {
        return toAjax(labelService.insertLabel(label));
    }

    /**
     * 修改标签系统
     */
    @PreAuthorize("@ss.hasPermi('system:label:edit')")
    @Log(title = "标签系统", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody Label label)
    {
        return toAjax(labelService.updateLabel(label));
    }

    /**
     * 删除标签系统
     */
    @PreAuthorize("@ss.hasPermi('system:label:remove')")
    @Log(title = "标签系统", businessType = BusinessType.DELETE)
	@DeleteMapping("/{ids}")
    public AjaxResult remove(@PathVariable Long[] ids)
    {
        return toAjax(labelService.deleteLabelByIds(ids));
    }
}
