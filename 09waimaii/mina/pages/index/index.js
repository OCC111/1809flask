//login.js
//获取应用实例
var app = getApp();
Page({
    data: {
        remind: '加载中',
        angle: 0,
        userInfo: {},
        isLogin: false
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
        this.checkLogin()
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
    login: function (e) {
        var that = this
        wx.getUserInfo({
            success(res) {
                if (!res.userInfo) {
                    // app.alert({'content':'获取用户数据失败,请稍后再试'})
                    return;
                }
                var data = res.userInfo
                wx.login({
                    success(res) {
                        if (res.code) {
                            // 发起网络请求
                            data['code'] = res.code
                            wx.request({
                                url: app.buildUrl('v1/user/login'),
                                data: {
                                    code: res.code,
                                    nickname: e.detail.userInfo.nickName,
                                    avatarUrl: e.detail.userInfo.avatarUrl,
                                    gender: e.detail.userInfo.gender,
                                },
                                method: 'POST',
                                header: app.getRequestHeader(),
                                success: function (res) {
                                    var data = res.data;
                                    if (data.code != 1) {
                                        app.alert({'content': data.msg});


                                    }
                                    if (data.code == 1) {
                                        app.setCache('token', res.data.data.token)

                                        that.goToIndex()
                                    }

                                }
                            })
                        } else {
                            console.log('登录失败！' + res.errMsg)
                        }
                    }
                })
            }
        });
    },
    checkLogin: function () {
        var that = this;
        wx.getUserInfo({
            success(res) {
                if (!res.userInfo) {
                    app.alert({'content': '获取用户数据失败,请稍后再试'})

                }
                var data = res.userInfo;
                wx.login({
                    success(res) {
                        if (res.code) {
                            // 发起网络请求
                            data['code'] = res.code;
                            wx.request({
                                url: app.buildUrl('v1/user/checkLogin'),
                                data: {'code': res.code},
                                method: 'POST',
                                header: app.getRequestHeader(),
                                success: function (res) {
                                    var data = res.data;
                                    // console.log(data.code)
                                    if (data.code == 1) {
                                        app.setCache('token', res.data.data.token)

                                        that.setData({
                                            isLogin: true
                                        })
                                    }

                                },
                            })
                        } else {
                            console.log('登录失败！' + res.errMsg)
                        }
                    }
                })
            }
        });
    }
});