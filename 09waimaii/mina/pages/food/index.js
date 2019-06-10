//index.js
//获取应用实例
var app = getApp();
Page({
    data: {
        indicatorDots: true,
        autoplay: true,
        interval: 3000,
        duration: 1000,
        loadingHidden: false, // loading
        swiperCurrent: 0,
        categories: [],
        activeCategoryId: 0,
        goods: [],
        scrollTop: "0",
        loadingMoreHidden: true,
        searchInput: '',
        banners: []
    },
    onLoad: function () {
        var that = this;

        wx.setNavigationBarTitle({
            title: app.globalData.shopName
        });

        that.setData({
            banners: [],
            categories: [
                {id: 0, name: "全部"},
                {id: 1, name: "川菜"},
                {id: 2, name: "东北菜"},
            ],
            activeCategoryId: 0,
            goods: [
                {
                    "id": 1,
                    "name": "小鸡炖蘑菇-1",
                    "min_price": "15.00",
                    "price": "15.00",
                    "pic_url": "/images/food.jpg"
                },
                {
                    "id": 2,
                    "name": "小鸡炖蘑菇-1",
                    "min_price": "15.00",
                    "price": "15.00",
                    "pic_url": "/images/food.jpg"
                },
                {
                    "id": 3,
                    "name": "小鸡炖蘑菇-1",
                    "min_price": "15.00",
                    "price": "15.00",
                    "pic_url": "/images/food.jpg"
                },
                {
                    "id": 4,
                    "name": "小鸡炖蘑菇-1",
                    "min_price": "15.00",
                    "price": "15.00",
                    "pic_url": "/images/food.jpg"
                }

            ],
            loadingMoreHidden: false
        });
        //调用后台接口
        this.getBannerAndCategory()
    },
    scroll: function (e) {
        var that = this, scrollTop = that.data.scrollTop;
        that.setData({
            scrollTop: e.detail.scrollTop
        });
    },
    //事件处理函数
    swiperchange: function (e) {
        this.setData({
            swiperCurrent: e.detail.current
        })
    },
    listenerSearchInput: function (e) {
        this.setData({
            searchInput: e.detail.value
        });
    },
    toSearch: function (e) {
        this.setData({
            p: 1,
            goods: [],
            loadingMoreHidden: true
        });
        this.getFoodList();
    },
    tapBanner: function (e) {
        if (e.currentTarget.dataset.id != 0) {
            wx.navigateTo({
                url: "/pages/food/info?id=" + e.currentTarget.dataset.id
            });
        }
    },
    toDetailsTap: function (e) {
        wx.navigateTo({
            url: "/pages/food/info?id=" + e.currentTarget.dataset.id
        });
    },
    getBannerAndCategory: function () {
        var that = this;
        wx.request({
            url: 'http://127.0.0.1:5000/api/v1/user/food', //仅为示例，并非真实的接口地址

            method: 'GET',
            header: app.getRequestHeader(),
            success  (res) {
                // console.log(res.data)
                var data = res.data;
                if (data.code != 1) {
                    app.alert({'content': data.msg});
                    return;
                }

                that.setData({
                    banners: data.data.banners
                })
            }
        })
    }
});


