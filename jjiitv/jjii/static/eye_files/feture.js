$(function() {
    $(".header-m-search-btn").click(function() {
        $(".top-search-all").toggle();
        $('.div-h').toggleClass("div-h2");
    });

    $(".menu-nav-btn").click(function() {
        $(".menu-nav-list").toggle();
        return false;
    });

    $(document).bind("click", function() {
        if ($('.menu-nav-list').css("display") == "block") {
            $('.menu-nav-list').hide();
        }
    });

    $("img.lazy").lazyload({
        effect: "fadeIn",
        threshold: 300,
        failurelimit: 10
    });
    $("img.lazy0").lazyload();
    $("img.lazy1").lazyload();
    $("img.lazy2").lazyload();

    var heightNum = $(".pdt-bread").height();
    $(".pdt-right").css("top", heightNum);


});


function setCookie(name, value, time) {
    var strsec = getsec(time);
    var exp = new Date();
    exp.setTime(exp.getTime() + strsec * 1);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString() + ";path=/";
}

function getsec(str) {
    var str1 = str.substring(1, str.length) * 1;
    var str2 = str.substring(0, 1);
    if (str2 == "s") {
        return str1 * 1000;
    } else if (str2 == "h") {
        return str1 * 60 * 60 * 1000;
    } else if (str2 == "d") {
        return str1 * 24 * 60 * 60 * 1000;
    }
}


function getCookies(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");

    if (arr = document.cookie.match(reg))

        return unescape(arr[2]);
    else
        return null;
}
setCookie("varify_key", "cleanpng", "d30");

function hits_process(id, hl) {
    $.get("https://topdata.downloadatoz.com/caicai_android_data_hits/proc/hits_process.php?id=" + id + "&hl=" + hl);
}

$("a.pdt-header-btn").click(function() {
    $.get("/search/", { keyword: $("input.pdt-header-input").val() });
    var e = $("input.pdt-header-input").val().toLowerCase().replace(/ /g, "-").replace(/'/g, "");
    if ("" != e && "search-png-images" != e) {
        var t = "https://www.cleanpng.com/free/" + e + ".html";
        window.location.href = t
    }
});
$("input.pdt-header-input").keydown(function(e) {
    if (13 == e.which) {
        $.get("/search/", { keyword: $("input.pdt-header-input").val() });
        var t = $("input.pdt-header-input").val().toLowerCase().replace(/ /g, "-").replace(/'/g, "");
        if ("" != t && "search-png-images" != t) {
            var i = "https://www.cleanpng.com/free/" + t + ".html";
            window.location.href = i
        }
    };
});
$(".top-search-submit").click(function() {
    $.get("/search/", { keyword: $("input.top-search-text").val() });
    var e = $("input.top-search-text").val().toLowerCase().replace(/ /g, "-");
    if ("" != e && "search-png-images" != e) {
        var t = "https://www.cleanpng.com/free/" + e + ".html";
        window.location.href = t
    }
});
$("input.top-search-text").keydown(function(e) {
    if (13 == e.which) {
        $.get("/search/", { keyword: $("input.top-search-text").val() });
        var t = $("input.top-search-text").val().toLowerCase().replace(/ /g, "-");
        if ("" != t && "search-png-images" != t) {
            var i = "https://www.cleanpng.com/free/" + t + ".html";
            window.location.href = i
        }
    };
});
$(".header-search-btn").click(function() {
    $.get("/search/", { keyword: $(".header-search-input").val() });
    var e = $(".header-search-input").val().toLowerCase().replace(/ /g, "-").replace(/'/g, "");
    if ("" != e && "search-png-images" != e) {
        var t = "https://www.cleanpng.com/free/" + e + ".html";
        window.location.href = t
    }
});
$("input.header-search-input").keydown(function(e) {
    if (13 == e.which) {
        $.get("/search/", { keyword: $(".header-search-input").val() });
        var t = $(".header-search-input").val().toLowerCase().replace(/ /g, "-").replace(/'/g, "");
        if ("" != t && "search-png-images" != t) {
            var i = "https://www.cleanpng.com/free/" + t + ".html";
            window.location.href = i
        }
    }
});
$(".pdt-header-input").focus(function() {
    $(".pdt-header-search").addClass("pdt-top-border");
    $(this).attr("placeholder", "");
});
$(".pdt-header-input").blur(function() {
    $(".pdt-header-search").removeClass("pdt-top-border");
    $(this).attr("placeholder", "Search PNG images");
});
$(".header-search-input").focus(function() {
    $(".header-search-box").addClass("home-search-border");
    $(this).attr("placeholder", "");
});
$(".header-search-input").blur(function() {
    $(".header-search-box").removeClass("home-search-border");
    $(this).attr("placeholder", "Search PNG images");
});

$(".top-search-text").focus(function() {
    $(".top-search-box").addClass("pdt-top-border-m");
    $(this).attr("placeholder", "");
});
$(".top-search-text").blur(function() {
    $(".top-search-box").removeClass("pdt-top-border-m");
    $(this).attr("placeholder", "Search PNG images");
});
$(".new-home-tag-btn span").click(function() {
    $(".new-home-tags").css("height", "auto");
    $(this).parent(".new-home-tag-btn").hide();
});
function getImage() {
    var img = event.srcElement;
    img.src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKAQMAAAC3/F3+AAAAA3NCSVQICAjb4U/gAAAABlBMVEX///8AAABVwtN+AAAAAnRSTlMAM8lDrC4AAAAJcEhZcwAACxIAAAsSAdLdfvwAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDkvMjEvMjPiBqWOAAAAHHRFWHRTb2Z0d2FyZQBBZG9iZSBGaXJld29ya3MgQ1M26LyyjAAAAA5JREFUCJlj+H+AATcCAAdSEXeho034AAAAAElFTkSuQmCC";
    img.onerror = null
}