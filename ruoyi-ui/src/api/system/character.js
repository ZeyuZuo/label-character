import request from "@/utils/request";
import axios from "axios";
import qs from 'qs'

// 查询人物信息
export function listPerson(query) {
  // return request({
  //   url: 'http://localhost:12345/persons',
  //   method: 'get',
  //   params: query
  // })
  return axios({
    url: 'http://localhost:12345/persons',
    method: 'GET',
    params: query
  });
}

export function getPersonInfo(id_card, tag_num) {
  if(tag_num === 5) {
    return axios({
      url: 'http://localhost:12345/person/info',
      method: 'get',
      params: {id_card}
    })
  }else{
    return axios({
      url: 'http://localhost:12345/person/tag',
      method: 'get',
      params: {id_card, tag_num}
    })
  }
}

export function getPersonTag(id_card) {
  return axios({
    url: 'http://localhost:12345/person/tags',
    method: 'get',
    params: {id_card}
  })
}
