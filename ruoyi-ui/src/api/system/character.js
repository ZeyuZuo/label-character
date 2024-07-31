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
