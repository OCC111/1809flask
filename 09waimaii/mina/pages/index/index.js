//login.js
//获取应用实例
var app = getApp();
Page({
    data: {
        remind: '加载中',
        angle: 0,
        userInfo: {},
        islogin: true
    },
    goToIndex: function () {
        wx.switchTab({
            url: '/pages/food/index',
        });
    },
    onLoad: function () {
        wx.setNavigationBarTitle({
            title: app.globalData.shopName
        })
    },
    onShow: function () {

    },
    onReady: function () {
        var that = this;
        setTimeout(function () {
            that.setData({
                remind: ''
            });
        }, 1000);
        wx.onAccelerometerChange(function (res) {
            var angle = -(res.x * 30).toFixed(1);
            if (angle > 14) {
                angle = 14;
            } else if (angle < -14) {
                angle = -14;
            }
            if (that.data.angle !== angle) {
                that.setData({
                    angle: angle
                });
            }
        });
    },
    bindGetUserInfo(e) {
        var that = this;
        wx.login({
            success(res) {
                if (res.code) {
                    //发起网络请求
                    console.log(res.code);
                    wx.request({
                        url: 'http://127.0.0.1:5000/api/v1/user/login', //仅为示例，并非真实的接口地址
                        data: {
                            code: res.code,
                            nickname: e.detail.userInfo.nickName,
                            avatarUrl: e.detail.userInfo.avatarUrl,
                            gender: e.detail.userInfo.gender,

                        },
                        method: 'POST',
                        header: app.getRequestHeader(),
                        success(res) {
                            var data = res.data;
                            if (data.code == 1) {
                                that.goToIndex()
                            }

                        }

                    })
                }else{
                    console.log('登录失败' + res.errMsg)
                }
            }
        });
        console.log(e.detail.userInfo)
    },

        checkUserInfo(e) {
        var that = this;
        wx.login({
            success(res) {
                if (res.code) {
                    //发起网络请求
                    console.log(res.code);
                    wx.request({
                        url: 'http://127.0.0.1:5000/api/v1/user/cklogin', //仅为示例，并非真实的接口地址
                        data: {
                            code: res.code,

                        },
                        method: 'POST',
                        header: app.getRequestHeader(),
                        success(res) {
                            var data = res.data;
                            if (data.code == 1) {
                                that.setData({
                                    islogin:true
                                })
                            }

                        }

                    })
                }
            }
        });
        console.log(e.detail.userInfo)
    }

});