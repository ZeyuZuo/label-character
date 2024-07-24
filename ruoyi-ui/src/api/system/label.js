import request from '@/utils/request'

// 查询标签系统列表
export function listLabel(query) {
  return request({
    url: '/system/label/list',
    method: 'get',
    params: query
  })
}

// 查询标签系统详细
export function getLabel(id) {
  return request({
    url: '/system/label/' + id,
    method: 'get'
  })
}

// 新增标签系统
export function addLabel(data) {
  return request({
    url: '/system/label',
    method: 'post',
    data: data
  })
}

// 修改标签系统
export function updateLabel(data) {
  return request({
    url: '/system/label',
    method: 'put',
    data: data
  })
}

// 删除标签系统
export function delLabel(id) {
  return request({
    url: '/system/label/' + id,
    method: 'delete'
  })
}
