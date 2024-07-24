drop table if exists sys_label;
create table sys_label (
        id        bigint(20)      not null auto_increment    comment 'id',
        parent_id         bigint(20)      default 0                  comment '父标签id',
        name      varchar(30)     not null               comment '标签名称',
        primary key (id)
) auto_increment=1 comment = '标签系统';

-- 菜单 SQL
insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('标签系统', '3', '1', 'label', 'system/label/index', 1, 0, 'C', '0', '0', 'system:label:list', '#', 'admin', sysdate(), '', null, '标签系统菜单');

-- 按钮父菜单ID
SELECT @parentId := LAST_INSERT_ID();

-- 按钮 SQL
insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('标签系统查询', @parentId, '1',  '#', '', 1, 0, 'F', '0', '0', 'system:label:query',        '#', 'admin', sysdate(), '', null, '');

insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('标签系统新增', @parentId, '2',  '#', '', 1, 0, 'F', '0', '0', 'system:label:add',          '#', 'admin', sysdate(), '', null, '');

insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('标签系统修改', @parentId, '3',  '#', '', 1, 0, 'F', '0', '0', 'system:label:edit',         '#', 'admin', sysdate(), '', null, '');

insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('标签系统删除', @parentId, '4',  '#', '', 1, 0, 'F', '0', '0', 'system:label:remove',       '#', 'admin', sysdate(), '', null, '');

insert into sys_menu (menu_name, parent_id, order_num, path, component, is_frame, is_cache, menu_type, visible, status, perms, icon, create_by, create_time, update_by, update_time, remark)
values('标签系统导出', @parentId, '5',  '#', '', 1, 0, 'F', '0', '0', 'system:label:export',       '#', 'admin', sysdate(), '', null, '');