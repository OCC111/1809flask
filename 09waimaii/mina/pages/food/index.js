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
        banners: [],
        page: 1,
        ismore: 1,
        isLoading: false,

    },
    onLoad: function () {
        var that = this;

        wx.setNavigationBarTitle({
            title: app.globalData.shopName
        });


        //调用后台接口
        this.getBannerAndCategory();
        this.getGoods();
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
            page: 1,
            goods: [],
            loadingMoreHidden: true
        });
        this.getFoodList();
    },
    tapBanner: function (e) {
        if (e.currentTarget.dataset.id != 0) {
            wx.navigateTo({
                url: "/pages/food/info?id=" + e.currentTarget.dataset.id
                // url: "/images/food.jpg"
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
            url: app.buildUrl('v1/food'),
            method: 'GET',
            header: app.getRequestHeader(),
            success: function (res) {
                var data = res.data;
                if (data.code != 1) {
                    app.alert({'content': data.msg});
                    return
                } else {
                    that.setData({
                        banners: data.data.banners,
                        categories: data.data.categories,

                    })
                }


            }
        })
    },
    getGoods: function () {
        var that = this;
        if (that.data.isLoading == true) {
            return
        }


        that.setData({
            isLoading: true
        });

        wx.request({
            url: app.buildUrl('v1/food/getGoods'),
            method: 'GET',
            data: {
                'cid': that.data.activeCategoryId,
                'page': that.data.page,
            },
            header: app.getRequestHeader(),
            success(res) {
                that.setData({
                    isLoading: false
                });

                if (res.data.code != 1) {
                    app.alert({'content': res.data.msg});
                    return;
                }


                if (res.data.code == 1) {

                    if (res.data.data.ismore == 0) {
                        that.setData({
                            loadingMoreHidden: false
                        })

                    }

                    that.setData({
                        goods: that.data.goods.concat(res.data.data.goods),
                        ismore: res.data.data.ismore,
                    })

                }
            }
        })
    },


    onReachBottom: function () {
        console.log('该加载数据了');
        var that = this ;

        //如果后端有数据再发送请求
        if (this.data.ismore == 1) {
            if (this.data.isLoading == false) {
                that.setData({
                    page: that.data.page + 1
                });
            }


            this.getGoods()
        }
    },
    catclick: function (e) {
        var that = this;
        // console.log(e.target.id);


        that.setData({
            activeCategoryId: e.target.id,
            page: 1,
            goods: [],
        });
        this.getGoods()

    },

});


// getGoods: function() {
//   var that = this;
//
//   if (that.data.isLoading == true){
//       return
//   }
//
//
//   that.setData({
//     isLoading:true  // 正在加载,保证当前内容正在加载的时候,不会有其他的再发起请求
//                     // 在网络加载缓慢的时候才可以显示出来
//   });
//   wx.request({
//     url: app.buildUrl('v1/food/getGoods'),
//     method: 'GET',
//     header: app.getRequestHeader(),
//     data: {
//       'categoryId': that.data.activeCategoryId,
//       'page':that.data.page
//     },
//       page:1,
//     success: function(res) {
//       var data = res.data;
//
//       if (data.code != 1) {
//         app.alert({ 'content': data.msg });
//
//         return
//       }
//       if (data.data.hasGoods == 0) {
//         that.setData({
//           hasGoods: false,
//           loadingMoreHidden: false
//         });
//
//       }
//       that.setData({
//         goods: that.data.goods.concat(data.data.goods),
//         // isLoading :false
//           ismore:res.data.data.ismore
//
//       })
//
//     }
//   })
// },


