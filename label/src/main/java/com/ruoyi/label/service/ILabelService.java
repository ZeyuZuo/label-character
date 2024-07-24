package com.ruoyi.label.service;

import java.util.List;
import com.ruoyi.label.domain.Label;

/**
 * 标签系统Service接口
 * 
 * @author ZeyuZuo
 * @date 2024-07-24
 */
public interface ILabelService 
{
    /**
     * 查询标签系统
     * 
     * @param id 标签系统主键
     * @return 标签系统
     */
    public Label selectLabelById(Long id);

    /**
     * 查询标签系统列表
     * 
     * @param label 标签系统
     * @return 标签系统集合
     */
    public List<Label> selectLabelList(Label label);

    /**
     * 新增标签系统
     * 
     * @param label 标签系统
     * @return 结果
     */
    public int insertLabel(Label label);

    /**
     * 修改标签系统
     * 
     * @param label 标签系统
     * @return 结果
     */
    public int updateLabel(Label label);

    /**
     * 批量删除标签系统
     * 
     * @param ids 需要删除的标签系统主键集合
     * @return 结果
     */
    public int deleteLabelByIds(Long[] ids);

    /**
     * 删除标签系统信息
     * 
     * @param id 标签系统主键
     * @return 结果
     */
    public int deleteLabelById(Long id);
}
