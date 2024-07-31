package com.ruoyi.label.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ruoyi.label.mapper.LabelMapper;
import com.ruoyi.label.domain.Label;
import com.ruoyi.label.service.ILabelService;

/**
 * 标签系统Service业务层处理
 * 
 * @author ZeyuZuo
 * @date 2024-07-24
 */
@Service
public class LabelServiceImpl implements ILabelService 
{
    @Autowired
    private LabelMapper labelMapper;

    /**
     * 查询标签系统
     * 
     * @param id 标签系统主键
     * @return 标签系统
     */
    @Override
    public Label selectLabelById(Long id)
    {
        return labelMapper.selectLabelById(id);
    }

    /**
     * 查询标签系统列表
     * 
     * @param label 标签系统
     * @return 标签系统
     */
    @Override
    public List<Label> selectLabelList(Label label)
    {
        return labelMapper.selectLabelList(label);
    }

    /**
     * 新增标签系统
     * 
     * @param label 标签系统
     * @return 结果
     */
    @Override
    public int insertLabel(Label label)
    {
        return labelMapper.insertLabel(label);
    }

    /**
     * 修改标签系统
     * 
     * @param label 标签系统
     * @return 结果
     */
    @Override
    public int updateLabel(Label label)
    {
        return labelMapper.updateLabel(label);
    }

    /**
     * 批量删除标签系统
     * 
     * @param ids 需要删除的标签系统主键
     * @return 结果
     */
    @Override
    public int deleteLabelByIds(Long[] ids)
    {
        for(Long id : ids){
            deleteLabelById(id);
        }
        return 1;
    }

    /**
     * 删除标签系统信息
     * 
     * @param id 标签系统主键
     * @return 结果
     */
    @Override
    public int deleteLabelById(Long id)
    {
        System.out.println("deleteLabelById: " + id);

        Label tmp = new Label();
        tmp.setParentId(id);
        List<Label> children = labelMapper.selectLabelList(tmp);
        if(children.isEmpty()){
            System.out.println("deleteLabelById: " + id + " is leaf");
            return labelMapper.deleteLabelById(id);
        }
        for(Label child : children) {
            deleteLabelById(child.getId());
        }
        return labelMapper.deleteLabelById(id);
    }
}
