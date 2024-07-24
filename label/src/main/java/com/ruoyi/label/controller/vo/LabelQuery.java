package com.ruoyi.label.controller.vo;


import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class LabelQuery {
    private String name;
    private String parentName;

    @Override
    public String toString() {
        return "LabelName(name=" + this.getName() + ", parentName=" + this.getParentName() + ")";
    }
}
