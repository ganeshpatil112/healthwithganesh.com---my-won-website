<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' b:templateUrl='vegeclub.xml' b:templateVersion='1.3.3' expr:dir='data:blog.languageDirection' expr:lang='data:blog.locale' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
  <head>
    <meta content='913648CB6413C9E3F34CF6AF68615F7D' name='msvalidate.01'/>
    <meta content='c592c1b006c52da1' name='yandex-verification'/>
    <meta content='width=device-width, initial-scale=1' name='viewport'/>
    <title><data:view.title.escaped/></title>
    <b:include data='blog' name='all-head-content'/>
    <title>
		<b:if cond='data:blog.pageType == &quot;index&quot;'>
			<data:blog.pageTitle/>
		<b:else/>
			<b:if cond='data:blog.pageType != &quot;error_page&quot;'>
				<data:blog.pageName/> - <data:blog.title/>
			<b:else/>
				ERROR 404 - <data:blog.title/> 
			</b:if>
		</b:if>
    </title>
    <!-- Description and Keywords (start) -->
    <b:if cond='data:blog.pageType == &quot;index&quot;'>
    <meta content='YOUR DESCRIPTION HERE' name='description'/>
    </b:if>
    <meta content='YOUR KEYWORDS HERE' name='keywords'/>
    <!-- Description and Keywords (end) -->
    <b:if cond='data:blog.pageType == &quot;item&quot;'>
        <meta expr:content='data:blog.pageName' property='og:title'/>
        <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
        <meta content='article' property='og:type'/>
    </b:if>
    <b:if cond='data:blog.postImageUrl'>
        <meta expr:content='data:blog.postImageUrl' property='og:image'/>
    <b:else/>
    <b:if cond='data:blog.postImageThumbnailUrl'>
        <meta expr:content='data:blog.postImageThumbnailUrl' property='og:image'/>
    </b:if></b:if>
    <b:if cond='data:blog.metaDescription != &quot;&quot;'>
        <meta expr:content='data:blog.metaDescription' name='og:description'/>
    </b:if>
    <meta expr:content='data:blog.title' property='og:site_name'/>
    <meta expr:content='data:blog.homepageUrl' name='twitter:domain'/>
    <meta expr:content='data:blog.pageName' name='twitter:title'/>
    <b:if cond='data:blog.postImageUrl'>
      <meta content='summary_large_image' name='twitter:card'/>
      <meta expr:content='data:blog.postImageUrl' name='twitter:image'/>
    <b:else/>
      <meta content='summary' name='twitter:card'/>
      <b:if cond='data:blog.postImageThumbnailUrl'>
        <meta expr:content='data:blog.postImageThumbnailUrl' name='twitter:image'/> 
      </b:if>
    </b:if>
    <meta expr:content='data:blog.pageName' name='twitter:title'/>
    <b:if cond='data:blog.metaDescription'>
      <meta expr:content='data:blog.metaDescription' name='twitter:description'/>
    </b:if>
    <!-- Social Media meta tag need customer customization -->
    <meta content='Facebook App ID here' property='fb:app_id'/> 
    <meta content='Facebook Admin ID here' property='fb:admins'/> 
    <meta content='@username' name='twitter:site'/>
    <meta content='@username' name='twitter:creator'/>    

<b:skin><![CDATA[/* 
-----------------------------------------------
Blogger Template Style
Name:        Sports Mag
Author :     http://www.healthwithganesh.com
License:     Free Version
------------------------------------ ----------- */

/* Variable definitions
=======================
<Variable name="keycolor" description="Main Color" type="color" default="#1e87f0" value="#f0871e"/>
<Variable name="body.background" description="Background" type="background" color="#ffffff" default="$(color) url() repeat scroll top left" value="#fbb1b2 url(https://themes.googleusercontent.com/image?id=1IgO1wWgj0K_rUZAoQza9BXyXF8I_PEFrP-DP9u0fUqePLlRNOTLtrSyYQglz9OZfPNqD) repeat fixed top center /* Credit: merrymoonmary (http://www.istockphoto.com/portfolio/merrymoonmary?platform=blogger) */"/>

<Group description="Main Settings" selector="body">
  <Variable name="main.color" description="Main Theme Color" type="color" default="#ef4d1c" value="#ef4d1c"/>
  <Variable name="main.dark.color" description="Main Dark Color" type="color" default="#202020" value="#202020"/>
  <Variable name="main.bb.color" description="Borders and Buttons Color" type="color" default="#272727" value="#272727"/>
  <Variable name="main.text.color" description="Main Text Color" type="color" default="$(main.dark.color)" value="#202020"/>
  <Variable name="body.font" description="Main Font" type="font" default="normal normal 14px Poppins" value="normal normal 13px Georgia, Utopia, &#39;Palatino Linotype&#39;, Palatino, serif"/>
</Group>
======================= 
*/

/* Reset and Variable Apply Here */
a,abbr,acronym,address,applet,b,big,blockquote,body,caption,center,cite,code,dd,del,dfn,div,dl,dt,em,fieldset,font,form,h1,h2,h3,h4,h5,h6,html,i,iframe,img,ins,kbd,label,legend,li,object,p,pre,q,s,samp,small,span,strike,strong,sub,sup,table,tbody,td,tfoot,th,thead,tr,tt,u,ul,var{padding:0;border:0;outline:0;vertical-align:baseline;background:0 0}
ins{text-decoration:underline}
del{text-decoration:line-through}
blockquote{font-size:15px;line-height:1.5em;font-style:italic;color:$(main.text.color)}
dl,ul{list-style-position:inside;font-weight:700;list-style:none}
ul li{list-style:none}
caption,th{text-align:center}
img{border:none;position:relative}
a,a:visited{text-decoration:none}
.clear{clear:both}
.section,.widget,.widget ul{margin:0;padding:0}
a{color:$(main.color)}
a:hover{color:$(main.color)}
:focus{outline:0}
a img{border:0}
brc{color:#bdbdbd}
.CSS_LIGHTBOX{z-index:999999!important}
.separator a{clear:none!important;float:none!important;margin-left:0!important;margin-right:0!important}
#navbar-iframe{display:none;height:0;visibility:hidden}
.widget-item-control,a.quickedit{display:none!important}
.archive .home-link,.index .home-link,.home-link{display:none!important}
*{outline:0;transition:all .3s ease;-webkit-transition:all .3s ease;-moz-transition:all .3s ease;-o-transition:all .3s ease}
:after,:before{transition:all .0s ease;-webkit-transition:all .0s ease;-moz-transition:all .0s ease;-o-transition:all .0s ease}
.status-msg-wrap{margin:0 auto 25px;text-transform:uppercase;font-size:11px}
.status-msg-border{border:1px solid #eee;opacity:.7;border-radius:2px}
.status-msg-bg{background-color:#f8f8f8;opacity:1;filter:none}
.feed-links{clear:both;display:none;line-height:2.5em}

/* Body */
body{background:$(body.background);font:$(body.font);color:#4f4f4f;word-wrap:break-word;margin:0;padding:0}
#outer-wrapper{max-width:1070px;margin:0 auto 20px;background-color:#FFF;}
.row{width:1070px}
#content-wrapper{margin:35px auto 5px;overflow:hidden}
.item #content-wrapper,.static_page #content-wrapper{margin:30px auto}
#main-wrapper{float:left;overflow:hidden;width:68%;word-wrap:break-word}
#sidebar-wrapper{float:right;overflow:hidden;width:32%;padding-left:2%;box-sizing:border-box;word-wrap:break-word;padding-bottom:20px}
#main-wrapper #main {margin-right:2%;}
.index #main-wrapper,.archive #main-wrapper{margin-top:10px;}
.home #main-wrapper{margin-top:0}
#topnav{width:100%;background-color:#333333;margin:0;    height: 36px;}
.tm-head{margin:0 auto;line-height:40px;overflow:hidden}
.tm-menu{float:left}
#nav1 li{    float: left;
    display: inline-block;
    height: 36px;
    line-height: 36px;
    margin-right: 18px;
    padding: 0;}
#nav1 li a{color:#ffffff;font-size:11px;font-weight:500;letter-spacing:.5px;text-transform:uppercase}
#nav1 li a:hover{color:$(main.color)}
.selectnav{display:none;background-color:$(main.bb.color);padding:2px 5px;box-sizing:border-box;border:0;}
select{background: url(data:image/svg+xml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZGF0YS1uYW1lPSJMYXllciAxIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0Ljk1IDEwIj48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9LmNscy0ye2ZpbGw6IzQ0NDt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPmFycm93czwvdGl0bGU+PHJlY3QgY2xhc3M9ImNscy0xIiB3aWR0aD0iNC45NSIgaGVpZ2h0PSIxMCIvPjxwb2x5Z29uIGNsYXNzPSJjbHMtMiIgcG9pbnRzPSIxLjQxIDQuNjcgMi40OCAzLjE4IDMuNTQgNC42NyAxLjQxIDQuNjciLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMy41NCA1LjMzIDIuNDggNi44MiAxLjQxIDUuMzMgMy41NCA1LjMzIi8+PC9zdmc+) no-repeat 95% 50%;
	-moz-appearance: none; 
	-webkit-appearance: none; 
	appearance: none;}
.social-area{float:right;    margin-right: -5px;}
.tm-head #social-top{position:relative;display:block;margin-right:0}
.tm-head #social-top ul{overflow:hidden}
.tm-head #social-top ul li{    height: 36px;
    line-height: 36px;
    display: block;
    float: left;

    padding: 0 5px;}
.tm-head #social-top ul li a{    color: #fff;
    display: inline-block;
    height: 25px;
    line-height: 25px;
    text-align: center;
    width: 25px;
    border-radius: 4px;    font-size: 12px;}
.tm-head #social-top ul li a:before{display:inline-block;font-family:FontAwesome;font-style:normal;font-weight:400;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}
.tm-head #social-top ul li a:hover{color:$(main.color)}
#social-top .facebook:before{content:"\f09a"}
#social-top .twitter:before{content:"\f099"}
#social-top .gplus:before{content:"\f0d5"}
#social-top .rss:before{content:"\f09e"}
#social-top .youtube:before{content:"\f167"}
#social-top .skype:before{content:"\f17e"}
#social-top .stumbleupon:before{content:"\f1a4"}
#social-top .tumblr:before{content:"\f173"}
#social-top .vine:before{content:"\f1ca"}
#social-top .stack-overflow:before{content:"\f16c"}
#social-top .linkedin:before{content:"\f0e1"}
#social-top .dribbble:before{content:"\f17d"}
#social-top .soundcloud:before{content:"\f1be"}
#social-top .behance:before{content:"\f1b4"}
#social-top .digg:before{content:"\f1a6"}
#social-top .instagram:before{content:"\f16d"}
#social-top .pinterest:before{content:"\f0d2"}
#social-top .delicious:before{content:"\f1a5"}
#social-top .codepen:before{content:"\f1cb"}




#social-top .facebook { background:#3C599F; }
#social-top .twitter { background:#32CCFE; }
#social-top .instagram { background:#A1755C; }
#social-top .pinterest {	background:#cb2027; }
#social-top .gplus { background:#dd4b39; }
#social-top .bloglovin {	background:#36ADED; }
#social-top .rss { background:#f26522; }
#social-top .youtube { background:#bb0000;}
#social-top .tumblr { background:#314E6C; }
#social-top .dribbble { background:#F46899; }
#social-top .soundcloud { background:#FF5500;}
#social-top .vimeo {	background:#229ACC; }
#social-top .linkedin {	background:#0085AE; }
#social-top .whatsapp {	background:#128c7e; }

#header-blog{height:90px;position:relative;overflow:hidden;padding:30px 0}
.header-content{margin:0 auto;overflow:hidden;height:90px}
.header-logo{float:left;width:285px;max-height:60px;margin:18px 0 0}
.header-logo img{max-width:100%;height:auto;margin:0}
.Header h1{color:$(main.text.color);margin:0;font-size:20px;line-height:1.3em}
.header-ads{float:right;width:728px;height:90px}
#menu{display:none}
#main-nav{position:relative;width:100%;height:48px;font-size:12px;margin:0 auto;    background-color: #fff;
    border-radius: 0;
    -webkit-border-radius: 0;
    -moz-border-radius: 0;
    -ms-border-radius: 0;
    -o-border-radius: 0;
    border-bottom: 1px solid #eee;
    margin-bottom: 0;
    transition: all ease 0.4s;
    -webkit-transition: all ease 0.4s;
    -moz-transition: all ease 0.4s;
    -o-transition: all ease 0.4s;
    z-index: 99;}
.header-menu{height:48px;margin:0 auto;position:relative;padding:0}
li.li-home{display:inline-block;position:relative;float:left;height:48px;box-sizing:border-box;padding:0;    padding: 0 30px 0 0; }
li.li-home a{    float: left;

 
    line-height: 51px;
    text-transform: uppercase;
    font-weight: 500;
    letter-spacing: .5px;
    color: $(main.color);}
li.li-home:hover{color: $(main.color);}
li.li-home:hover a{color:#fff}
#main-nav ul li{position:relative;float:left;height:48px;box-sizing:border-box;padding:0;    padding: 0 30px 0 0;}
#main-nav ul li a{float:left;color:#333;    line-height:51px;text-transform:uppercase;font-weight:500;letter-spacing:.5px}
#main-nav ul li:hover{ color: $(main.color);}
#main-nav ul li:hover a{ color: $(main.color);}
#main-nav ul li.has-children a{padding-right:0px}
#main-nav ul li.has-children a:after{content:"\f067";font-family:FontAwesome;font-size:8px;font-weight:400;position:absolute;top:0;right:14px}
#main-nav ul li ul{display:none;position:absolute;left:0;top:48px;z-index:100;background-color:$(main.dark.color);border-top:0;box-shadow:0 1px 3px rgba(40,35,40,0.05);transition:all 0s ease;-webkit-transition:all 0s ease;-moz-transition:all 0s ease;-o-transition:all 0s ease}
#main-nav ul li ul li{height:auto;margin-left:0;display:block;float:none;position:relative;overflow:hidden;line-height:normal;padding:0;border-right:0;border-bottom:1px solid $(main.bb.color)}
#main-nav ul li ul li:last-child{border-bottom:0}
#main-nav ul li ul li a{min-width:180px;color:#F2F2F2;font-size:10px;font-weight:500;text-transform:uppercase;height:34px;line-height:34px;overflow:hidden;box-sizing:border-box;padding:0 16px!important;margin-top:0;border:0;transition:all .3s ease!important;-webkit-transition:all .3s ease!important;-moz-transition:all .3s ease!important;-o-transition:all .3s ease!important}
#main-nav ul li:hover ul li a{color:#F2F2F2}
#main-nav ul li ul li a:after{display:none}
#main-nav ul li ul li a:hover{background-color:$(main.color);color:#fff!important;padding-left:20px!important}
@keyframes slideInDown {
from{-webkit-transform:translate3d(0,-100%,0);transform:translate3d(0,-100%,0);visibility:visible}
to{-webkit-transform:translate3d(0,0,0);transform:translate3d(0,0,0)}
}
#search-icon{position:absolute;right:0;top:0;display:block;line-height:48px;height:48px;color:#333;font-size:16px;padding:0;text-align:center;cursor:pointer;}
#search-icon:hover{color:$(main.color);}
#nav-search{position:absolute;right:0;top:48px;z-index:50;display:none;width:300px;height:54px;background-color:$(main.bb.color);border:0;border-top:0;border-radius:0;transition:all 0s ease;-webkit-transition:all 0s ease;-moz-transition:all 0s ease;-o-transition:all 0s ease;box-sizing:border-box}
#nav-search #searchform{width:100%;position:relative;margin:10px 0;padding:0 10px;box-sizing:border-box;height:34px;overflow:hidden;border-radius:0}
#nav-search #s{width:100%;box-sizing:border-box;position:relative;height:34px;float:left;padding:0 10px;margin:0;border:0;background-color:#fff;font-size:12px;font-family:inherit;color:#F2F2F2;border-radius:0}
#nav-search #s:focus{color:#F2F2F2;outline:none}
.featured{position:relative;margin:30px auto 0}
.featured .widget-content{margin:0px 0 0!important;height:auto;overflow:hidden}
.featured h2{display:none}
.featured .feat-align{    float: left;
    width: 25%;
    padding-right: 1px;
    box-sizing: border-box;
    }
.feat-align.feat-column1 {
    width: 50%;padding: 0 8px;
}
.featured .hot-item{width:100%;height:195px;position:relative;float:left;display:block;box-sizing:border-box;overflow:hidden;padding:0}
.featured .feat-column1 .item1{height:399px;   }
.featured .feat-column1 .item1 .rcp-thumb{height:403px}
.featured .feat-column2 .item3{margin-top:8px;   }

.featured .feat-column4 {padding-right: 0;}

.featured .feat-column4 .item5{margin-top:8px;    }
.featured .hot-item .featured-inner{position:relative;overflow:hidden}
.featured .rcp-thumb{width:100%;height:195px;position:relative;display:block;overflow:hidden;   }
.featured .rcp-title{font-size:16px;position:relative;margin-bottom:8px}

.item3 .rcp-thumb:after{content:no-close-quote;height:190px}
.featured .post-panel{position:absolute;left:0;bottom:0;width:100%;padding:15px;z-index:2;box-sizing:border-box;    text-align: right;}
.featured .hot-item .featured-inner .featured-meta{font-size:12px;color:#ccc;font-weight:400}
.featured .rcp-title a{color:#FFF;font-weight:500;position:relative;line-height:1.4em;text-shadow:0 1px 1px rgba(0,0,0,0.5)}
.featured .post-tag{       background-color: $(main.color);
    color: #fff;
    text-transform: uppercase;
    font-weight: 400;
    z-index: 5;
    height: 20px;
    line-height: 32px;
    padding: 0 6px;
    font-size: 11px;}
.featured{position:relative}
.featured-overlay{position:absolute;left:0;top:0;z-index:1;width:100%;height:100%;background-color:rgba(40,35,40,0.05)}
.featured .hot-item:hover .featured-overlay{background-color:rgba(40,35,40,0.30)}
.recent-boxes{overflow:hidden;position:relative}
.box-sec{margin-right:2%}
.box-sec h2{display:none}
.recent-boxes .box-sec .widget:last-child{margin-bottom:20px}
.box-title,.posts-title{position:relative;clear:both;z-index:1;margin-bottom:10px;line-height:33px}
.box-title h2.title,.posts-title h2.title{display:inline-block;position:relative;background-color:#fff;color:$(main.text.color);font-size:15px;letter-spacing:-.4px;text-transform:uppercase;font-weight:700;z-index:1;margin:0;padding-right:15px;    padding-left: 25px;}
.sidebar .widget h2:before,.box-title h2.title:before, .posts-title h2.title:before {
    position: absolute;
    content: "";
    width: 12px;
    height: 12px;
    display: inline-block;
    background-color: $(main.color);
    left: 0;
    top: 49%;
    -webkit-transform: translateY(-49%);
    -ms-transform: translateY(-49%);
    transform: translateY(-49%);
    z-index: 5;
}

.sidebar .widget h2:before, .box-title h2.title:before:nth-child(1), .posts-title h2.title:before:nth-child(1){background-color: #66297e;}


.social-count-plus ul {
    border: none !important;
    list-style: none !important;
    margin: 0;
    padding: 0;
}
.social-count-plus li {
    background: none !important;
    border: none !important;
    clear: none !important;
    float: left;
    list-style: none !important;
    margin: 0;
    padding: 0 0 20px;
    text-align: center;
    width: 60px;
}

.social-count-plus .flat li {
    margin-right: 1px;
    width: 32%;
    background: #9a9a9a!important;
    padding-top: 5px;
    padding-bottom: 5px;
    margin-bottom: 7px;
}

.social-count-plus .flat li.count-twitter {
    background: #2181c3!important;
}

.social-count-plus .flat .count-twitter a {
    background-position: 0px 0 !important;
}

.social-count-plus .flat a {
    background-image: url(https://4.bp.blogspot.com/-X7NN6bB_BE0/WIpygw0-5vI/AAAAAAAAJmw/PJhnRCS3dz8oaKuiq-yFPGsNJ2N1tPfdACLcB/s1600/sprite-flat.png) !important;
    height: 32px !important;
    width: 32px !important;
}

.social-count-plus a {
    -moz-transition: all .4s ease;
    -o-transition: all .4s ease;
    -webkit-transition: all .4s ease;
    transition: all .4s ease;
    display: block;
    margin: 0 auto;
    opacity: 1;
    padding: 0 !important;
}


.social-count-plus span {
    display: block;
    margin: 0;
    padding: 0;
}

.social-count-plus .count {
    display: block;
    font-size: 14px;
    font-weight: bold;
    line-height: 16px;
    margin: 5px 0 0;
    padding: 0;
}

.social-count-plus .label {
    font-size: 9px;
    font-weight: normal;
    line-height: 16px;
    text-transform: capitalize;
}

.social-count-plus .flat li.count-facebook {
    background: #345897!important;
}

.social-count-plus .flat .count-facebook a {
    background-position: -32px 0 !important;
}

.social-count-plus .flat a {
    background-image: url(https://4.bp.blogspot.com/-X7NN6bB_BE0/WIpygw0-5vI/AAAAAAAAJmw/PJhnRCS3dz8oaKuiq-yFPGsNJ2N1tPfdACLcB/s1600/sprite-flat.png) !important;
    height: 32px !important;
    width: 32px !important;
}

.social-count-plus .flat li.count-googleplus {
    background: #ec4b3d!important;
}
.social-count-plus .flat .count-googleplus a {
    background-position: -96px 0 !important;
}
.social-count-plus .flat a {
    background-image: url(https://4.bp.blogspot.com/-X7NN6bB_BE0/WIpygw0-5vI/AAAAAAAAJmw/PJhnRCS3dz8oaKuiq-yFPGsNJ2N1tPfdACLcB/s1600/sprite-flat.png) !important;
    height: 32px !important;
    width: 32px !important;
}


.social-count-plus:after {
    content: "";
    display: table;
    clear: both;
}

.social-count-plus a:hover {
    opacity: 0.7;
}


.box-title h2.title a,.posts-title h2.title a{color:$(main.text.color)}
.box-title:after,.posts-title:after{content:"";position:absolute;z-index:0;top:12px;left:0;width:99%;    border: 4px double #eee;}
.recent-boxes .widget{margin-bottom:30px}
.boxes .bx-first .box-thumbnail{position:relative;width:100%;height:343px}
.boxes .bf-thumb{width:100%;height:343px;position:relative;display:block}
.box-thumbnail{overflow:hidden}
.boxes ul li .box-thumbnail{width:90px;height:70px;display:table-cell;vertical-align:middle}
.boxes ul li .box-image{width:90px;height:70px;position:relative;display:block}
.bx-first .box-thumbnail .first-tag{position:absolute;top:15px;left:15px;z-index:2}
.bx-first .box-thumbnail .first-tag a{background:$(main.color);color:#fff;text-transform:uppercase;height:20px;line-height:20px;display:inline-block;padding:0 6px;font-size:11px;font-weight:400}
.boxes ul li .recent-content{display:table-cell;padding-left:15px;padding-right:5px}
.boxes .recent-title a:hover{color:$(main.color)}
.recent-boxes .fbox,.recent-boxes .videos{width:100%;float:left}
.fbox .bx-first{width:50%;position:relative;float:left;padding-right:1.4%;box-sizing:border-box;overflow:hidden}
.fbox .bx-item{width:100%;position:relative;overflow:hidden}
.fbox .bx-first .bf-content{position:absolute;bottom:0;width:100%;z-index:2;padding:15px;box-sizing:border-box}
.fbox .bx-first .bf-content .recent-title a{display:block;font-size:18px;color:#fff;font-weight:500;line-height:1.5em;text-shadow:0 .5px .5px rgba(34,34,34,0.3);margin-bottom:8px}
.fbox li .recent-content .recent-title{overflow:hidden;line-height:0;margin:0 0 3px;padding:0}
.fbox li .recent-content .recent-title a{color:$(main.text.color);font-weight:500;font-size:14px;line-height:1.5em}
.boxes ul li .recent-content .recent-title a:hover{color:$(main.color)}
.bx-first .bf-thumb:after{content:no-close-quote;position:absolute;left:0;bottom:0;width:100%;height:151px;background:url(http://3.bp.blogspot.com/-LnvazGBvKh8/VskckSkmzxI/AAAAAAAAC4s/erEgI6A_ih4/s1600-r/metabg.png) repeat-x;opacity:.8}
.bf-content .recent-date{color:#ccc}
.fbox ul li{display:block;width:48.6%;float:right;margin:0 0 10px;padding:0 0 10px;border-bottom:1px dotted #f5f5f5}
.fbox ul li:last-child{margin-bottom:0;padding-bottom:0;border-bottom:0}
.img-overlay{position:absolute;left:0;top:0;z-index:1;width:100%;height:100%;background-color:rgba(40,35,40,0.05)}
.tk-thumb a:hover .img-overlay,.boxes ul li .box-image:hover .img-overlay,.boxes .bx-first:hover .img-overlay,.custom-widget .rcthumb:hover .img-overlay,.PopularPosts .item-thumbnail:hover a .img-overlay,.map-thumb:hover .img-overlay{background-color:rgba(40,35,40,0.3)}
.videos .recent-title a{display:block;font-size:18px;color:$(main.text.color);font-weight:500;line-height:1.5em;margin-bottom:5px}
.videos .recent-title a:hover{color:$(main.color)}
.videos ul{position:relative;overflow:hidden}
.videos ul li{width:50%;float:left;box-sizing:border-box;margin:0;padding:0 5px 0 0}
.videos ul li:nth-child(2){padding:0 0 0 5px}
.videos ul li .videos-item{width:100%;position:relative;display:block;overflow:hidden;padding:0}
.videos .box-image{width:100%;height:220px;display:block;position:relative;margin:0;padding:0}
.videos .box-image:before{content:"\f04b";font-family:FontAwesome;line-height:54px;width:54px;height:54px;font-size:20px;color:#fff;text-align:center;background-color:RGBA(0,0,0,0.4);font-weight:400;position:absolute;top:50%;right:50%;margin-top:-27px;margin-right:-27px;opacity:.5;z-index:2;padding:0;border:2px solid #fff;border-radius:50%;transition:all .3s ease}
.videos li:hover .box-image:before{opacity:1}
.videos .recent-content{width:100%;z-index:2;padding:10px 10px 0 0;text-align:left;box-sizing:border-box;position:relative}
.videos-overlay{position:absolute;left:0;top:0;z-index:1;width:100%;height:100%;background-color:rgba(40,35,40,0.0)}
.videos li:hover .videos-overlay{background:rgba(40,35,40,0.3)}
.recent-boxes .carousel{position:relative;margin:0 0 25px!important;padding:0;overflow:visible;height:auto;display:block;clear:both}
.main-carousel{overflow:hidden}
.carousel-item{padding:0!important;position:relative;overflow:hidden;list-style:none}
.carousel-thumb{width:100%;height:250px;position:relative;display:block}
.carousel-item .box-image{width:100%;height:250px;position:relative;display:block}
.carousel-item .box-image:after{content:no-close-quote;position:absolute;left:0;bottom:0;width:100%;height:171px;background:url(http://3.bp.blogspot.com/-LnvazGBvKh8/VskckSkmzxI/AAAAAAAAC4s/erEgI6A_ih4/s1600-r/metabg.png) repeat-x;background-size:100% 100%;opacity:.8}
.carousel-content{position:absolute;bottom:0;width:100%;z-index:2;box-sizing:border-box;padding:15px;text-align:left}
.carousel-item .recent-title{margin:10px 0 3px;font-size:16px;font-weight:500}
.carousel-item .recent-title a{color:#fff;display:inline-block;line-height:1.4em;text-shadow:0 .5px .5px rgba(34,34,34,0.3)}
.carousel-item .recent-date{color:#ccc}
.carousel-tag a{display:inline-block;background-color:$(main.color);color:#fff;height:20px;line-height:20px;padding:0 6px;font-size:11px;text-transform:uppercase}
.carousel-overlay{position:absolute;left:0;top:0;z-index:1;width:100%;height:250px;background-color:rgba(40,35,40,0.05)}
.main-carousel .owl-item:hover .carousel-overlay{background-color:rgba(40,35,40,0.30)}
.main-carousel .owl-prev,.main-carousel .owl-next{margin-top:0;width:40px;height:40px;font-size:25px;line-height:40px}
.main-carousel .owl-prev{left:-50px}
.main-carousel:hover .owl-prev{left:0}
.main-carousel .owl-next{right:-50px}
.main-carousel:hover .owl-next{right:-1px}
.main-carousel .owl-dots{bottom:10px}
.recent-date{color:#bdbdbd;font-size:12px;font-weight:400}
.recent-date:before,.featured-date:before{content:'\f017';font-family:fontawesome;margin-right:5px}
.owl-carousel .animated{-webkit-animation-duration:1000ms;animation-duration:1000ms;-webkit-animation-fill-mode:both;animation-fill-mode:both}
.owl-carousel .owl-animated-in{z-index:0}
.owl-carousel .owl-animated-out{z-index:1}
.owl-carousel .fadeOut{-webkit-animation-name:fadeOut;animation-name:fadeOut}
@-webkit-keyframes fadeOut {
0%{opacity:1}
100%{opacity:0}
}
@keyframes fadeOut {
0%{opacity:1}
100%{opacity:0}
}
.owl-height{-webkit-transition:height 500ms ease-in-out;-moz-transition:height 500ms ease-in-out;-ms-transition:height 500ms ease-in-out;-o-transition:height 500ms ease-in-out;transition:height 500ms ease-in-out}
.owl-carousel{display:none;width:100%;-webkit-tap-highlight-color:transparent;position:relative;z-index:1}
.owl-carousel .owl-stage{position:relative;-ms-touch-action:pan-Y}
.owl-carousel .owl-stage:after{content:".";display:block;clear:both;visibility:hidden;line-height:0;height:0}
.owl-carousel .owl-stage-outer{position:relative;overflow:hidden;-webkit-transform:translate3d(0px,0px,0px)}
.owl-carousel .owl-controls .owl-nav .owl-prev,.owl-carousel .owl-controls .owl-nav .owl-next,.owl-carousel .owl-controls .owl-dot{cursor:pointer;cursor:hand;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}
.owl-carousel.owl-loaded{display:block}
.owl-carousel.owl-loading{opacity:0;display:block}
.owl-carousel.owl-hidden{opacity:0}
.owl-carousel .owl-refresh .owl-item{display:none}
.owl-carousel .owl-item{position:relative;min-height:1px;float:left;-webkit-backface-visibility:visible;-webkit-tap-highlight-color:transparent;-webkit-touch-callout:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}
.owl-carousel .owl-item img{display:block;width:100%;-webkit-transform-style:preserve-3d;transform-style:preserve-3d}
.owl-carousel.owl-text-select-on .owl-item{-webkit-user-select:auto;-moz-user-select:auto;-ms-user-select:auto;user-select:auto}
.owl-carousel .owl-grab{cursor:move;cursor:-webkit-grab;cursor:-o-grab;cursor:-ms-grab;cursor:grab}
.owl-carousel.owl-rtl{direction:rtl}
.owl-carousel.owl-rtl .owl-item{float:right}
.no-js .owl-carousel{display:block}
.owl-prev,.owl-next{top:0;color:$(main.text.color);background-color:rgba(255,255,255,0.8);font-family:FontAwesome;position:absolute;z-index:1;display:block;padding:0;cursor:pointer;padding:0;text-align:center;overflow:hidden}
.owl-prev{left:0}
.owl-prev:before{content:"\f104"}
.owl-next{right:0}
.owl-next:before{content:"\f105"}
.owl-prev:hover,.owl-next:hover{background-color:rgba(23,23,23,0.9);color:#f2f2f2}
.owl-dots{position:absolute;bottom:1px;width:33.33%;left:0;right:0;margin:auto;text-align:center}
.owl-dot{background:#fff;height:3px;width:10px;display:inline-block;margin:0 5px;-webkit-border-radius:2px;-moz-border-radius:2px;border-radius:2px;opacity:.6}
.owl-dot.active,.owl-dot:hover{background:$(main.color)}
.custom-widget li{overflow:hidden;padding:10px 0;border-top:1px dotted #f5f5f5}
.custom-widget .rcthumb{position:relative;float:left;margin:0!important;width:90px;height:70px;overflow:hidden;display:block;vertical-align:middle}
.custom-widget .post-panel{padding-left:15px;display:table-cell}
.custom-widget .rcp-title{overflow:hidden;line-height:0;margin:0 0 3px;padding:0}
.custom-widget .rcp-title a{color:$(main.text.color);font-weight:500;font-size:13px;line-height:1.5em}
.custom-widget .rcp-title a:hover{color:$(main.color)}
.cmm-widget li .cmm-avatar{position:relative;overflow:hidden;padding:0;width:55px;height:55px;float:left;margin:0 10px 0 0}
.cmm-widget li{background:none!important;clear:both;list-style:none;word-break:break-all;display:block;border-top:1px dotted #F5F5F5;overflow:hidden;margin:0;padding:10px 0}
.cmm-widget li:first-child{padding-top:0;border-top:0}
.cmm-widget li:last-child{padding-bottom:0}
.cmm-widget li span{margin-top:4px;color:#bdbdbd;display:block;line-height:1.2em;text-transform:lowercase;font-size:12px;font-style:italic;font-weight:400}
.cmm-img{width:55px;height:55px;float:left;margin:0 10px 0 0}
.cmm-widget a{color:$(main.text.color);position:relative;font-size:14px;font-weight:500;display:block;overflow:hidden}
.cmm-widget a:hover{color:$(main.color)}
.cmm-widget{list-style:none;padding:0}
.home-ad .widget{padding-right:2%}
.home-ad .widget-content{width:728px;max-height:90px;padding:0;margin:0 auto 15px;max-width:100%;box-sizing:border-box}
.header-ads h2,#ads-home h2,#post-ads-footer h2{display:none!important}
.posts-title{margin-right:2%}
.post{display:block;overflow:hidden;word-wrap:break-word}
.index .post,.archive .post{margin:0 0 15px;padding-bottom:15px;border-bottom:1px dotted #f5f5f5}
.index div.post-outer:last-child .post,.archive div.post-outer:last-child .post{padding-bottom:5px;border-bottom:0}
.block-image{position:relative;float:left;width:290px;height:190px;margin-right:20px}
.block-image .thumb{width:100%;height:190px;position:relative;display:block;z-index:2;overflow:hidden}
.block-image .thumb a{width:100%;height:190px;display:block}
.thumb-overlay{position:absolute;left:0;top:0;z-index:2;width:100%;height:100%;background-color:rgba(40,35,40,0.05)}
.block-image:hover .thumb a .thumb-overlay,.related-posts .related-item:hover .related-thumb a .thumb-overlay{background-color:rgba(40,35,40,0.30)}
.retitle h2{margin:8px 0;display:block}
.post h2 a,.post h2 a:visited,.post h2 strong{color:$(main.text.color);font-size:19px;line-height:1.5em;font-weight:500;text-decoration:none}
.post h2 a:hover{color:$(main.color)}
.widget iframe,.widget img{max-width:100%}
.index .post-footer,.archive .post-footer{display:none!important}
.index .post h2,.archive .post h2{margin:0 0 8px;padding:0 10px 0 0;overflow:hidden}
.item .post,.static_page .post{padding:0}
.date-header{display:block;overflow:hidden;font-weight:400;margin:0!important;padding:0}
#meta-post{font-size:12px;color:#bdbdbd;line-height:1.4em}
#meta-post a{color:#bdbdbd}
#meta-post .timestamp-link{margin-left:0}
#meta-post .timestamp-link abbr:before{content:'\f017';font-family:fontawesome;color:#bdbdbd;margin-right:5px}
.resumo{margin-top:10px;font-size:13px;color:#919191;line-height:1.5em}
.resumo span{display:block;margin-bottom:8px;padding-right:10px}
a.read-more{display:inline-block;margin-bottom:0;font-weight:500;text-align:left;vertical-align:middle;cursor:pointer;background-image:none;white-space:nowrap;line-height:25px;height:25px;color:#fff;background-color:#000;border-radius:0;font-size:11px;text-transform:uppercase;padding:0 10px;margin-top:3px;outline:none;border:none;overflow:hidden;    border-left: 6px solid $(main.color);}
.post-meta{color:#bdbdbd;display:block;font-size:12px;font-weight:400;line-height:21px;margin:0;padding:0}
.postags{position:absolute;top:15px;left:15px;z-index:3}
.postags a{display:inline-block;display:none;background:$(main.color);color:#fff;margin:0;height:20px;line-height:20px;padding:0 6px;font-size:11px;text-transform:uppercase}
.postags a:first-child{display:inline-block}
.breadcrumbs{margin:0;font-size:12px;margin-bottom: 10px;color: #777;}
.breadcrumbs brc {
    color: #7c7c7c;
    display: inline-block;
    font-size: 12px;
    padding: 0px 8px 0 5px;
}
.item article,.static_page article{margin-top:15px}
.item .post-head,.static_page .post-head{position:relative;margin:2px 0 5px}
.item .post-title,.static_page .post-title{color:$(main.text.color);font-size:24px;line-height:1.5em;font-weight:700;position:relative;display:inline-block;padding:0;margin:0}
.item .post-body,.static_page .post-body{width:100%;color:#5E5E5E;font-size:14px;line-height:1.7em;overflow:hidden}
.item .post-outer{padding:0}
.item .post-body img{max-width:100%}
.post-meta a{color:#bdbdbd}
.post-timestamp{margin-left:0}
.label-head{margin-left:0}
.label-head a{padding-left:2px}
.label-head a:hover{color:$(main.color)}
.post-meta .g-profile span:before{content:'\f007';font-family:fontawesome;color:#bdbdbd;margin-right:5px}
.post-meta .post-timestamp{margin-left:0px}
.post-meta .post-timestamp .timestamp-link abbr:before{content:'\f017';font-family:fontawesome;color:#bdbdbd;margin-right:5px}
.post-meta .label-head{margin-left:10px}
.post-meta .label-head:before{content:'\f07c';font-family:fontawesome;color:#bdbdbd;margin-right:0}
.main .widget{margin:0}
.main .Blog{border-bottom-width:0}

.share-art{position:relative;display:block;overflow:hidden;margin:20px 0;padding:15px 0;border-top:1px dotted #f0f0f0;border-bottom:1px dotted #f0f0f0}
.sa-title{display:block;float:left;height:30px;line-height:30px;margin:8px 15px 8px 0;padding:0}
.sa-title strong{font-size:16px;display:block}
.share-art a{float:left;font-size:12px;line-height:30px;color:#fff;-webkit-border-radius:2px;-moz-border-radius:2px;border-radius:2px;margin:8px 3px;padding:0 20px;height:30px;min-width:30px;text-align:center}
.share-art a:hover{background-color:#222;color:#fff}
.share-art a i.fa{margin-right:7px;font-size:12px}
.share-art .facebook{background-color:#003471}
.share-art .twitter{background-color:#00BFF3}
.share-art .googleplus{background-color:#EA4D29}
.share-art .pinterest{background-color:#C6393D}
.share-art .linkedin{background-color:#0077B5}
#related-wrap{margin-bottom:20px}
.related-title{position:relative;clear:both;z-index:1;margin:5px 0 10px;line-height:33px}
.related-title h2{display:inline-block;position:relative;background-color:#fff;color:$(main.text.color);font-size:16px;letter-spacing:-.4px;text-transform:uppercase;font-weight:700;z-index:1;margin:0;padding-right:15px}
.related-title:after{content:"";position:absolute;z-index:0;top:12px;left:0;width:100%;   border: 4px double #eee;}
.related-posts{position:relative;overflow:hidden;margin:0;padding:0}
.related-posts .related-item{width:33.33%;height:180px;position:relative;overflow:hidden;float:left;display:block;box-sizing:border-box;margin:0;padding:0 2.5px}
.related-posts li:first-child{padding-left:0}
.related-posts li:nth-child(3){padding-right:0}
.related-posts .related-item .related-img{width:100%;height:180px;position:relative;display:block}
.related-posts .related-item .related-img:after{content:no-close-quote;position:absolute;left:0;bottom:0;width:100%;height:120px;background:url(http://3.bp.blogspot.com/-LnvazGBvKh8/VskckSkmzxI/AAAAAAAAC4s/erEgI6A_ih4/s1600-r/metabg.png) repeat-x;background-size:100% 100%;opacity:.8}
.related-overlay{position:absolute;left:0;top:0;z-index:1;width:100%;height:100%;background-color:rgba(40,35,40,0.05)}
.related-posts .related-item:hover .related-overlay{background-color:rgba(40,35,40,0.30)}
.related-content{position:absolute;bottom:0;padding:15px 15px 11px;width:100%;line-height:1.2em;box-sizing:border-box;z-index:2}
.related-posts .related-tag{position:absolute;top:15px;left:15px;background-color:$(main.color);color:#fff;text-transform:uppercase;font-weight:400;z-index:5;height:20px;line-height:20px;padding:0 6px;font-size:11px}
.related-posts h3 a{font-size:14px;line-height:1.4em;padding:10px 0 4px;font-weight:500;color:#fff;display:block;text-shadow:0 .5px .5px rgba(34,34,34,0.3)}
.related-posts .related-item .recent-date{color:#ccc}
.featured .post-tag:hover,.carousel-tag a:hover,.bx-first .box-thumbnail .first-tag a:hover,.post-readmore a:hover,.postags a:hover,a.read-more:hover,.related-tag:hover{background:$(main.dark.color)}
.ib-nav li{padding:0;display:inline-block;width:50%}
.ib-nav li strong{display:block;padding:0 0 5px;font-weight:700;text-transform:uppercase;font-size:13px}
.ib-nav li strong i{transition:all 0s ease;-webkit-transition:all 0s ease;-moz-transition:all 0s ease;-o-transition:all 0s ease}
ul.ib-nav{background-color:#FFF;display:block;width:100%;position:relative;overflow:hidden;margin-bottom:15px;border-bottom:2px solid #f5f5f5;border-top:2px solid #f5f5f5}
.ib-nav li a{color:$(main.text.color);line-height:1.3em;display:block;padding:15px 0;transition:all 0s ease;-webkit-transition:all 0s ease;-moz-transition:all 0s ease;-o-transition:all 0s ease}
.ib-nav li:hover a{opacity:.6}
ul.ib-nav span{font-size:13px;font-weight:400}
.ib-nav .previous{float:left;min-height:80px;border-right:1px solid #f5f5f5;box-sizing:border-box;padding-right:10px}
.ib-nav .next{text-align:right;border-left:1px solid #f5f5f5;margin-left:-1px;padding-left:10px;box-sizing:border-box}
#blog-pager{clear:both;text-align:center;margin:0}
.index #blog-pager{display:block}
.index #blog-pager,.archive #blog-pager{padding:0 0 20px;text-align:left}
#blog-pager-newer-link a,#blog-pager-older-link a{display:block;float:left;margin-right:0;padding:0 12px;border:0;text-transform:uppercase;line-height:32px;font-weight:400;background-color:$(main.dark.color);color:#fff;font-size:12px}
#blog-pager-newer-link a:hover,#blog-pager-older-link a:hover{background-color:$(main.color)}
.showpageNum a,.showpage a,.showpagePoint{display:block;float:left;margin-right:6px;padding:0 12px;background:$(main.dark.color);color:#fff;border:0;text-transform:uppercase;line-height:32px;font-weight:500;border-radius:0}
.showpageNum a:hover,.showpage a:hover{background-color:$(main.color)}
.showpageNum a i,.showpage a i{transition:all 0s ease;-webkit-transition:all 0s ease;-moz-transition:all 0s ease;-o-transition:all 0s ease}
.showpagePoint{background-color:$(main.color);color:#fff}
.showpageOf{display:none!important}
.comments-title{position:relative;clear:both;z-index:1;margin:0;line-height:33px}
.comments-title h2{display:inline-block;position:relative;background-color:#fff;color:$(main.text.color);font-size:16px;letter-spacing:-.4px;text-transform:uppercase;font-weight:700;z-index:1;margin:0;padding-right:15px}
.comments-title:after{content:"";position:absolute;z-index:0;top:11px;left:0;width:100%;    border: 4px double #eee;}
.blogger-tab{display:block}
.comments{clear:both;margin:0;color:$(main.text.color)}
.comments h4{font-weight:400;font-size:12px;font-style:italic;padding-top:1px}
.comments .comments-content{margin:0;padding:0}
.comments .comments-content .comment{margin-bottom:0;padding-bottom:8px}
.comments .comments-content .comment:first-child{padding-top:0}
.facebook-tab,.fb_iframe_widget_fluid span,.fb_iframe_widget iframe{width:100%!important}
.comments .item-control{position:static}
.comments .avatar-image-container{float:left;overflow:hidden;position:absolute}
.comments .avatar-image-container,.comments .avatar-image-container img{height:45px;max-height:45px;width:45px;max-width:45px;border-radius:0}
.comments .comment-block{overflow:hidden;padding:0 0 10px}
.comments .comment-block,.comments .comments-content .comment-replies{margin-left:60px;margin-top:0}
.comments .comments-content .inline-thread{padding:0}
.comments .comment-actions{float:left;width:100%;position:relative;margin:0}
.comments .comments-content .comment-header{font-size:14px;display:block;overflow:hidden;clear:both;margin:0 0 3px;padding:0 0 5px;border-bottom:1px dotted #f5f5f5}
.comments .comments-content .user{font-style:normal;font-weight:500;display:block;font-size:16px}
.comments .comments-content .icon.blog-author{display:none}
.comments .comments-content .comment-content{float:left;text-align:left;font-size:13px;line-height:1.4em;color:#656565}
.comments .comment .comment-actions a{margin-right:5px;padding:2px 5px;color:$(main.text.color);font-weight:400;background-color:#f5f5f5;font-size:10px}
.comments .comment .comment-actions a:hover{color:#fff;background-color:$(main.color);text-decoration:none}
.comments .comments-content .datetime{color:#999;float:left;font-size:11px;position:relative;font-style:italic;margin:2px 0 0;display:block}
.comments .comments-content .datetime:before{content:'\f017';font-family:fontawesome;font-style:normal;margin-right:3px}
.comments .comments-content .comment-header a{color:inherit}
.comments .comments-content .comment-header a:hover{color:$(main.color)}
.comments .thread-toggle{margin-bottom:4px}
.comments .thread-toggle .thread-arrow{height:7px;margin:0 3px 2px 0}
.comments .thread-expanded{padding:8px 0 0}
.comments .comments-content .comment-thread{margin:0}
.comments .continue a{padding:0 0 0 60px;font-weight:400}
.comments .comments-content .loadmore.loaded{margin:0;padding:0}
.comments .comment-replybox-thread{margin:0}
iframe.blogger-iframe-colorize,iframe.blogger-comment-from-post{height:283px!important}
.post-body h1,.post-body h2,.post-body h3,.post-body h4,.post-body h5,.post-body h6{color:$(main.text.color);margin-bottom:15px}
blockquote{margin:0;padding:0 20px}
blockquote:before{content:'\f10d';display:inline-block;font-family:FontAwesome;font-style:normal;font-weight:400;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;margin-right:10px;color:$(main.text.color)}
blockquote:after{content:'\f10e';display:inline-block;font-family:FontAwesome;font-style:normal;font-weight:400;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;margin-left:10px;color:$(main.text.color)}
.widget .post-body ul,.widget .post-body ol{line-height:1.5;font-weight:400}
.widget .post-body li{margin:5px 0;padding:0;line-height:1.5}
.post-body ul li:before{content:"\f0da";margin-right:5px;font-family:fontawesome}
#sidebar-wrapper .widget{padding:0;background:#FFF;margin-bottom:30px;overflow:hidden}
.sidebar .widget .title-wrap{position:relative;z-index:1;margin-bottom:10px;line-height:33px}
.sidebar .widget h2{display:inline-block;position:relative;background-color:#fff;color:$(main.text.color);font-size:15px;letter-spacing:-.4px;text-transform:uppercase;font-weight:700;z-index:1;margin:0 0 10px;padding-right:15px;padding-left: 25px;}
.sidebar .widget .title-wrap h2{margin:0}
.sidebar .widget .title-wrap:after{content:"";position:absolute;z-index:0;top:12px;left:0;width:100%;    border: 4px double #eee;}
.sidebar ul{list-style:none}
.sidebar .widget-content{margin:0}
.list-label-widget-content li{display:block;padding:8px 0;border-bottom:1px dotted #F5F5F5;position:relative}
.list-label-widget-content li:first-child{padding:0 0 8px}
.list-label-widget-content li:last-child{padding-bottom:0;border-bottom:0}
.list-label-widget-content li a:before{content:'\203a';position:absolute;left:0;top:4px;font-size:22px;color:$(main.text.color)}
.list-label-widget-content li:first-child a:before{top:-5px}
.list-label-widget-content li a{color:$(main.text.color);font-size:12px;padding-left:15px;font-weight:500}
.list-label-widget-content li a:hover{color:$(main.color)}
.list-label-widget-content li span:last-child{color:#999;font-size:12px;font-weight:500;position:absolute;top:11px;right:0}
.list-label-widget-content li:first-child span:last-child{top:3px}
.cloud-label-widget-content{text-align:left}
.cloud-label-widget-content .label-count{background:$(main.color);color:#fff!important;margin-left:-3px;white-space:nowrap;border-radius:0;padding:1px 4px!important;font-size:12px!important;margin-right:5px}
.cloud-label-widget-content .label-size{    border: 1px solid #eee;display:block;float:left;font-size:11px;margin:0 5px 5px 0}
.cloud-label-widget-content .label-size a,.cloud-label-widget-content .label-size span{height:18px!important;color:$(main.text.color);display:inline-block;font-size:12px;font-weight:500!important;padding:6px 8px}
.cloud-label-widget-content .label-size a{padding:6px 10px}
.cloud-label-widget-content .label-size a:hover{color:#fff!important}
.cloud-label-widget-content .label-size,.cloud-label-widget-content .label-count{height:30px!important;line-height:19px!important}
.cloud-label-widget-content .label-size:hover{background:$(main.color);color:#fff!important}
.cloud-label-widget-content .label-size:hover a{color:#fff!important}
.cloud-label-widget-content .label-size:hover span{background:$(main.dark.color);color:#fff!important;cursor:pointer}
.cloud-label-widget-content .label-size-1,.label-size-2,.label-size-3,.label-size-4,.label-size-5{font-size:100%;opacity:10}
.label-size-1,.label-size-2{opacity:100}
.FollowByEmail td{width:100%;float:left;box-sizing:border-box}
.FollowByEmail .follow-by-email-inner .follow-by-email-submit{margin-left:0;width:100%;border-radius:0;height:30px;font-size:11px;color:#fff;background-color:$(main.color);font-family:inherit;text-transform:uppercase;font-weight:700;letter-spacing:1px}
.FollowByEmail .follow-by-email-inner .follow-by-email-submit:hover{background-color:$(main.bb.color)}
.FollowByEmail .follow-by-email-inner .follow-by-email-address{padding-left:10px;height:30px;border:1px solid #FFF;margin-bottom:5px;box-sizing:border-box;font-size:11px;font-family:inherit}
.FollowByEmail .follow-by-email-inner .follow-by-email-address:focus{border:1px solid #FFF}
.FollowByEmail .widget-content{background-color:$(main.dark.color);box-sizing:border-box;padding:10px}
.FollowByEmail .widget-content:before{content:"Enter your email address to subscribe to this blog and receive notifications of new posts by email.";font-size:11px;color:#f2f2f2;line-height:1.4em;margin-bottom:5px;display:block;padding:0 2px}
.flickr_widget .flickr_badge_image{float:left;margin-bottom:5px;margin-right:10px;overflow:hidden;display:inline-block}
.flickr_widget .flickr_badge_image:nth-of-type(4),.flickr_widget .flickr_badge_image:nth-of-type(8),.flickr_widget .flickr_badge_image:nth-of-type(12){margin-right:0}
.flickr_widget .flickr_badge_image img{max-width:67px;height:auto}
.flickr_widget .flickr_badge_image img:hover{opacity:.5}
#ArchiveList select{border:1px solid $(main.dark.color);padding:6px 8px;width:100%;cursor:pointer;font-family:inherit;font-size:12px;color:$(main.text.color)}
.PopularPosts .item-thumbnail{margin:0 15px 0 0 !important;width:90px;height:70px;float:left;overflow:hidden}
.PopularPosts .item-thumbnail a{position:relative;display:block;overflow:hidden;line-height:0}
.PopularPosts ul li img{padding:0;width:90px;height:70px}
.PopularPosts .widget-content ul li{overflow:hidden;padding:10px 0;border-top:1px dotted #f5f5f5}
.sidebar .PopularPosts .widget-content ul li:first-child,.sidebar .custom-widget li:first-child{padding-top:0;border-top:0}
.sidebar .PopularPosts .widget-content ul li:last-child,.sidebar .custom-widget li:last-child{padding-bottom:0}
.PopularPosts ul li a{color:$(main.text.color);font-weight:500;font-size:14px;line-height:1.5em}
.PopularPosts ul li a:hover{color:$(main.color)}
.PopularPosts .item-title{margin:0;padding:0;line-height:0}
.item-snippet{display:none;font-size:0;padding-top:0}
.contact-form-name,.contact-form-email,.contact-form-email-message,.contact-form-widget{max-width:none;margin-bottom:0;padding:0}
.contact-form-name,.contact-form-email,.contact-form-email-message{background-color:#f3f3f3;border:0}
.contact-form-button-submit{max-width:none;width:100%;height:30px;border:0;background-image:none;background-color:$(main.color);cursor:pointer;font-family:inherit;font-style:normal;font-weight:700;border-radius:0!important;text-transform:uppercase}
.contact-form-name:focus,.contact-form-email:focus,.contact-form-email-message:focus{border:0;box-shadow:none}
.contact-form-name:hover,.contact-form-email:hover,.contact-form-email-message:hover{border:0}
.contact-form-button-submit:hover{background-color:$(main.dark.color);background-image:none;border:0}
#footer-wrapper{background-color:$(main.dark.color)}
#footer{overflow:hidden;margin:0 auto;padding:0}
.sect-left{display:inline-block;float:left;width:32%;margin-right:2%}
.sect-left:nth-child(3){margin-right:0}
.sect-left .widget{padding:20px 0}
.sect-left .widget:nth-of-type(2){padding-top:0}
.sect-left .widget .title-wrap{position:relative;z-index:1;margin-bottom:10px;line-height:33px}
.sect-left .widget h2{display:inline-block;position:relative;background-color:$(main.dark.color);color:#F2F2F2;font-size:14px;letter-spacing:-.4px;text-transform:uppercase;font-weight:700;z-index:1;margin:0 0 10px;padding-right:15px}
.sect-left .widget .title-wrap h2{margin:0}
.sect-left .widget .title-wrap:after{content:"";position:absolute;z-index:0;top:13px;left:0;width:100%;height:5px;background-color:$(main.bb.color)}
.sect-left .custom-widget .rcp-title a,.sect-left .PopularPosts ul li a{color:#F2F2F2}
.sect-left .recent-date{color:#999999}
.sect-left .custom-widget li{overflow:hidden;border-color:$(main.bb.color);padding:10px 0}
.sect-left .PopularPosts .widget-content ul li{border-color:$(main.bb.color)}
.sect-left .PopularPosts .widget-content ul li:first-child,.sect-left .custom-widget li:first-child{padding-top:0;border-top:0}
.sect-left .custom-widget .rcp-title a:hover,.sect-left .PopularPosts ul li a:hover{color:$(main.color)}
.sect-left .cmm-widget li{border-color:$(main.bb.color)}
.sect-left .cmm-widget a{color:#F2F2F2}
.sect-left .cmm-widget a:hover{color:$(main.color)}
.sect-left .FollowByEmail .widget-content{background-color:$(main.bb.color)}
.sect-left .FollowByEmail .follow-by-email-inner .follow-by-email-submit:hover{background:$(main.dark.color)}
.sect-left .FollowByEmail .widget-content:before{content:"Enter your email address to subscribe to this blog and receive notifications of new posts by email.";color:#F2F2F2}
.sect-left #ArchiveList select{border:1px solid $(main.bb.color);background:$(main.bb.color);color:#F2F2F2}
.sect-left #ArchiveList select option{color:#F2F2F2}
.sect-left .cloud-label-widget-content .label-size{background:$(main.bb.color)}
.sect-left .cloud-label-widget-content .label-size:hover{background:$(main.color)}
.sect-left .cloud-label-widget-content .label-size a{color:#F2F2F2}
.cloud-label-widget-content .label-size:hover span{background:$(main.dark.color)}
.sect-left .list-label-widget-content li{border-bottom:0;border-top:1px dotted $(main.bb.color)}
.sect-left .list-label-widget-content li:first-child{border-top:0;padding-top:0}
.sect-left .list-label-widget-content li a,.sect-left .list-label-widget-content li a:before{color:#F2F2F2}
.sect-left .list-label-widget-content li a:hover{color:$(main.color)}
.sect-left .list-label-widget-content li:first-child a:before{top:-6px}
.footer-wrapper{background-color:RGBA(0,0,0,0.2);color:#F2F2F2;display:block;padding:10px 0;width:100%;height:30px;overflow:hidden}
.footer-wrapper .footer-copy{margin:0 auto}
.footer-wrapper .copyright{font-size:11px;float:left;height:30px;line-height:30px;font-weight:500;text-transform:uppercase;letter-spacing:.3px}
.footer-wrapper .copyright a{color:#F2F2F2}
.footer-wrapper .copyright a:hover{color:$(main.color)}
.native-opt{float:right}
.native-opt li{float:right;display:inline-block;list-style:none!important}
.native-opt li a{display:block;width:30px;height:30px;background-color:$(main.bb.color);text-align:center;color:#F2F2F2;line-height:30px;margin-left:10px;padding:0}
.native-opt li a:hover{background-color:$(main.color);color:#fff}
.error_page #main-wrapper{width:100%!important;margin:0!important}
.error_page #sidebar-wrapper,.error_page .status-msg-wrap{display:none}
#error-wrap{color:$(main.text.color);text-align:center;padding:60px 0 80px}
.error-item{font-size:160px;line-height:1;margin-bottom:20px}
#error-wrap h2{font-size:25px;padding:20px 0 10px}
#error-wrap .homepage{padding-top:10px;display:block}
#error-wrap .homepage i{font-size:20px}
#error-wrap .homepage:hover{text-decoration:underline}
div#ArchiveList a {
    color: #202020;
}
.img-anime .recent-boxes .box-image,.img-anime .recent-boxes .bf-thumb,.img-anime .custom-widget .rcthumb,.img-anime .PopularPosts img,.img-anime .home .block-image .thumb a,.img-anime .tc-thumb a,.img-anime .related-thumb a,.img-anime .PopularPosts .item-thumbnail a,.img-anime .cmm-img{opacity:0;transition:all 0s ease;-webkit-transition:all 0s ease;-moz-transition:all 0s ease;-o-transition:all 0s ease}
.img-anime .img-effect,.img-anime .recent-boxes .box-image.img-effect,.img-anime .recent-boxes .bf-thumb.img-effect,.img-anime .custom-widget .rcthumb.img-effect,.img-anime .PopularPosts img.img-effect,.img-anime .block-image .thumb a.img-effect,.img-anime .tc-thumb a.img-effect,.img-anime .related-thumb a.img-effect,.img-anime .PopularPosts .item-thumbnail a.img-effect,.img-anime .cmm-img.img-effect{opacity:1;transition:all .8s ease;-webkit-transition:all .8s ease;-moz-transition:all .8s ease;-o-transition:all .8s ease}
]]></b:skin>

<style type='text/css'>
/*----Responsive Design----*/
@media screen and (max-width: 1130px) {
.row{max-width:96%}
#main-nav{width:96%;max-width:96%}
#main-nav .row{max-width:100%}
.header-logo {width: 240px;}
}
@media screen and (max-width: 980px) {
#header-blog,.header-content{height:auto}
.header-logo{max-width:222px;margin:15px auto 30px;float:none;display:block}
.header-logo img{margin:0 auto}
.header-ads{max-width:100%;float:none;height:auto;margin:0 auto;display:block}
.header-ads .widget{line-height:0}
#main-wrapper{float:none;overflow:hidden;width:100%}
.recent-boxes .box-sec{margin-right:0}
.posts-title{margin-right:0}
#main-wrapper #main{margin-right:0}
#sidebar-wrapper{width:100%;margin:10px auto;float:none;padding-left:0}
#footer{padding:20px 0}
.sect-left{width:100%;margin-right:0}
.sect-left .widget{padding:10px}
}
@media screen and (max-width: 880px) {
#nav1,#menu-main-nav{display:none}
.selectnav{display:block;color:#eee}
.tm-menu{float:left;width:20%}
.tm-menu .selectnav{padding:0 5px;height:30px!important;    width: 110px;font-size:12px;line-height:22px;margin-top:5px;border-radius:2px!important;-moz-border-radius:2px!important;-webkit-border-radius:2px!important}
.header-menu #menu .selectnav{padding:0 10px!important;font-size:14px;height:35px;line-height:26px;margin-left:10px;float:left;border-radius:2px!important;margin-top:7px}
.featured .feat-align{width:33.33%;}
.feat-column1,.feat-column3{padding-left:0}
.feat-column2,.feat-column4,.feat-column5{padding-right:0}
.feat-column3,.feat-column4{margin-top:0px}
.home-ad .widget{padding-right:0}
}
@media screen and (max-width: 700px) {
#ticker{display:none}
.fbox .bx-first .box-thumbnail,.fbox .bf-thumb{height:250px}
.fbox .bx-first{width:100%;margin-bottom:0;padding-right:0;border-right:0}
.fbox ul li{width:100%;float:left;margin-top:10px;margin-bottom:0;padding-top:10px;padding-bottom:0;border-top:1px dotted #F5F5F5;border-bottom:0}
.recent-boxes .column{width:100%}
.block-image{width:100%;height:250px;margin-right:0}
.block-image .thumb,.block-image .thumb a{height:250px}
.main-carousel,.carousel-item,.carousel-item .box-image{height:250px}
.index .post article,.archive .post article{overflow:hidden;position:relative;float:left;margin-top:10px}
.owl-carousel .owl-item,.carousel-item{width:100%}
.videos ul li{width:100%;margin:0 0 15px}
.videos .box-image{height:250px}
.footer-wrapper{height:auto}
.footer-wrapper .copyright{text-align:center;float:none;height:auto;padding:0 0 10px}
.native-opt{float:none;display:block;text-align:center;overflow:hidden}
.native-opt li{float:none;display:inline-block}
.native-opt li a{margin:0}
}
@media screen and (max-width: 600px) {
.featured .feat-align{width:100%;margin-top:5px;padding-left:0;padding-right:0}
.feat-column1{margin-top:8px!important}
.featured .feat-column1 .item1,.featured .feat-column2 .item2,.featured .feat-column3 .item3,.featured .feat-column1 .item1 .rcp-thumb,.featured .feat-column2 .item2 .rcp-thumb,.featured .feat-column3 .item3 .rcp-thumb{height:250px}
.item .post-title,.static_page .post-title{font-size:24px}
.related-posts .related-item{width:100%;height:180px;margin-top:5px;padding:0}
.related-posts li:first-child{margin-top:0!important}
}
@media screen and (max-width: 440px) {
#nav-search{width:100%}
.featured .feat-column1 .item1,.featured .feat-column2 .item2,.featured .feat-column3 .item3,.featured .feat-column1 .item1 .rcp-thumb,.featured .feat-column2 .item2 .rcp-thumb,.featured .feat-column3 .item3 .rcp-thumb,.featured .rcp-thumb,.featured .hot-item{height:200px}
.main-carousel,.carousel-item,.carousel-item .box-image,.fbox .bx-first .box-thumbnail,.fbox .bf-thumb,.block-image,.block-image .thumb,.block-image .thumb a,.videos .box-image{height:200px}
.index .post h2,.archive .post h2{line-height:1.4em}
.post h2 a,.post h2 a:visited,.post h2 strong{font-size:20px;line-height:1.4em}
.item .post-title,.static_page .post-title{font-size:20px}
.fbox .bx-first .bf-content .recent-title a{font-size:16px}
}
@media screen and (max-width: 340px) {
.header-menu #menu .selectnav{max-width:60%}
.error-item{font-size:140px}
}
@media screen and (max-width: 310px) {
.tm-head #social-top ul li{margin-left:0}
.header-logo{margin:15px auto 10px}
.header-menu #menu .selectnav{max-width:50%}
.header-ads,li.li-home,#sidebar-wrapper,.sect-left{display:none}
.videos .recent-title a{font-size:16px}
.post h2 a,.post h2 a:visited,.post h2 strong{font-size:18px}
.index .post h2,.archive .post h2{line-height:1.2em}
.item .post-title,.static_page .post-title{font-size:16px}
.error-item{font-size:100px}
}
</style>

<b:template-skin><![CDATA[
/*------Layout (No Edit)----------*/
body#layout #outer-wrapper{padding:0;width:1073px}
body#layout .row {width: 1000px;}

body#layout .section h4{margin:2px 0 8px;color:#333!important}
body#layout .ibpanel{background-color:#2c3e50!important;overflow:hidden!important;border-color:#213243!important}
body#layout .ibpanel h4{font-size:16px;padding:0;color:#fff!important}
body#layout .ibpanel .widget{float:left;width:30%;margin-right:5%}
body#layout .ibpanel #HTML902,body#layout .ibpanel #HTML905{margin-right:0}
body#layout .ibpanel .widget.locked-widget .widget-content{background-color:#34495e!important;border-color:#455668!important;color:#fff!important}
body#layout .ibpanel .widget.locked-widget .widget-content a.editlink{color:#fff!important;border:1px solid #233648;border-radius:2px;padding:0 5px;background-color:#233648}
body#layout #topnav,body#layout .tm-head{height:auto}
body#layout .tm-menu{margin:0;width:70%}
body#layout .social-area{margin:0;width:30%}
body#layout .header-content,body#layout #header-blog{height:auto;padding:0}
body#layout .header-logo{float:left;width:30%;max-width:30%;max-height:none;margin:0;padding:0}
body#layout .header-logo #header{background-color:#b57dcc!important;border-color:#8a52a1!important}
body#layout .header-ads{height:auto;width:70%}
body#layout #menu,body#layout #menu1{display:block;background-color:#6dad88;border-color:#338957}
body#layout #main-nav,body#layout .header-menu{height:auto}
body#layout .header-menu li.li-home,body#layout .header-search{display:none}
body#layout .header-menu{float:left;width:100%;margin:4px 0 0;padding:0}
body#layout #content-wrapper{margin:0 auto}
body#layout .box-sec .widget-content,body#layout .box-sec h2,body#layout #ads-blog{display:block}
body#layout #main-wrapper{float:left;width:70%;margin:0;padding:0}
body#layout .posts-title{display:none}
body#layout #sidebar-wrapper{float:right;width:30%;margin:0;padding:5px 0 0;background-color:#f8e244!important}
body#layout #sidebar-wrapper .section{background-color:#fff;border:1px solid #fff}
body#layout #sidebar-wrapper .section .draggable-widget .widget-wrap2{background-color:#5a7ea2!important}
body#layout #footer-wrapper{overflow:hidden}
body#layout .sect-left{width:26%;float:left;margin:0 1% 8px !important}
body#layout #blocked-widgets,body#layout #pop-sec,body#layout #contact{display:none!important}
body#layout #featured-sec{background-color:#f9a85f;border-color:#fb8f3d}
body#layout #featured-sec .draggable-widget .widget-wrap2{background-color:#fb8f3d!important}
body#layout #featured-sec .add_widget{border-color:#fb8f3d}
body#layout #main-wrapper #main{margin-right:4px;background-color:#5a7ea2;border-color:#34495e}
body#layout #main-wrapper #main h4{color:#fff!important}
body#layout .layout-widget-description{display:none!important}
body#layout .box-sec{background-color:#7fc1ed!important;border-color:#3498db!important}
body#layout .box-sec .draggable-widget .widget-wrap2{background-color:#3498db!important;cursor:move}
body#layout .box-sec .add_widget{border-color:#3498db}
body#layout #sidebar{margin-top:10px}
body#layout .widget-content .editlink{color:#fff!important;border:1px solid #233648;border-radius:2px;padding:0 5px;background-color:#233648}
body#layout #footer{overflow:hidden;background-color:#1abc9c;padding-top:10px;margin-bottom:10px}
body#layout #footer:before{content:"Footer Sections";font-size:25px;color:#fff;padding:0 0 10px;text-align:center;display:block;font-family:raleway}
body#layout #footer .section .draggable-widget .widget-wrap2{background-color:#1abc9c!important}
body#layout #footer-sec3{margin-right:0}
body#layout #ads-content,body#layout #ads-home{background-color:rgba(241,196,16,0.22);border-color:#f1c410}
body#layout #ads-content .add_widget,body#layout #ads-home .add_widget{border-color:#f1c410!important}
body#layout #ads-content .draggable-widget .widget-wrap2,body#layout #ads-inter .draggable-widget .widget-wrap2,body#layout #ads-home .draggable-widget .widget-wrap2{background-color:#f1c410!important;cursor:move}
#layout:before {    content: 'This is the property of healthwithganesh.com';
text-transform: uppercase;
font-size: 20px;
color: #999;
margin: 0 0 20px 0;
display: inline-block;
font-weight: 700;
padding: 20px;
font-family: sans-serif;
border: 4px double #FD856E;}
body#layout .native-opt li{list-style:none}
/*------Layout (end)----------*/
]]></b:template-skin>

<b:include data='blog' name='google-analytics'/>
<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js' type='text/javascript'/>

</head>
<body expr:class='data:blog.pageType'>

  <div class='theme-opt' style='display:none'>
    <b:section class='ibpanel' id='ibpanel' maxwidgets='1' name='Theme Options' showaddelement='yes'>
      <b:widget id='HTML900' locked='true' title='Full Width CSS' type='HTML' version='1'>
        <b:widget-settings>
          <b:widget-setting name='content'/>
        </b:widget-settings>
        <b:includable id='main'>
          &lt;style&gt;@media only screen and (min-width:1133px){#outer-wrapper{max-width:<data:content/>;}}&lt;/style&gt;
        </b:includable>
      </b:widget>
      <b:widget id='HTML901' locked='true' title='Home Recent Posts Display' type='HTML' version='1'>
        <b:widget-settings>
          <b:widget-setting name='content'/>
        </b:widget-settings>
        <b:includable id='main'>
          &lt;style&gt;.home #main-wrapper #main,.home .posts-title{display:<data:content/>;}&lt;/style&gt;
        </b:includable>
      </b:widget>
      <b:widget id='HTML902' locked='true' title='Home PageNav Display' type='HTML' version='1'>
        <b:widget-settings>
          <b:widget-setting name='content'/>
        </b:widget-settings>
        <b:includable id='main'>
          &lt;style&gt;.home #blog-pager{display:<data:content/>;}&lt;/style&gt;
        </b:includable>
      </b:widget>
      <b:widget id='HTML904' locked='true' title='Related Posts Display' type='HTML' version='1'>
        <b:widget-settings>
          <b:widget-setting name='content'/>
        </b:widget-settings>
        <b:includable id='main'>
          &lt;style&gt;.item #related-wrap{display:<data:content/>;}&lt;/style&gt;
        </b:includable>
      </b:widget>
      <b:widget id='HTML905' locked='true' title='Item Post Navigation Display' type='HTML' version='1'>
        <b:widget-settings>
          <b:widget-setting name='content'/>
        </b:widget-settings>
        <b:includable id='main'>
          &lt;style&gt;.item ul.ib-nav{display:<data:content/>;}&lt;/style&gt;
        </b:includable>
      </b:widget>
    </b:section>
  </div>

<div id='top'/>


  <div id='topnav'>
    <div class='tm-head row'>
      <div class='tm-menu'>
        <b:section class='menu1' id='menu1' maxwidgets='1' name='Top Navigation' showaddelement='yes'>
          <b:widget id='LinkList210' locked='true' title='Menu' type='LinkList' version='1'>
            <b:widget-settings>
              <b:widget-setting name='link-5'>https://www.healthwithganesh.com/p/terms-and-conditions.html</b:widget-setting>
              <b:widget-setting name='link-3'>https://www.healthwithganesh.com/p/disclaimer.html</b:widget-setting>
              <b:widget-setting name='link-4'>https://www.healthwithganesh.com/p/privacy-policy.html</b:widget-setting>
              <b:widget-setting name='text-1'>About us</b:widget-setting>
              <b:widget-setting name='text-0'>Home</b:widget-setting>
              <b:widget-setting name='text-3'>Disclaimer</b:widget-setting>
              <b:widget-setting name='text-2'>contact</b:widget-setting>
              <b:widget-setting name='text-5'>Terms and conditions</b:widget-setting>
              <b:widget-setting name='text-4'>Privacy Policy</b:widget-setting>
              <b:widget-setting name='sorting'>NONE</b:widget-setting>
              <b:widget-setting name='link-1'>https://www.healthwithganesh.com/p/about-us.html</b:widget-setting>
              <b:widget-setting name='link-2'>https://www.healthwithganesh.com/p/contacts-us.html</b:widget-setting>
              <b:widget-setting name='link-0'>https://www.healthwithganesh.com/</b:widget-setting>
            </b:widget-settings>
            <b:includable id='main'>
              <div class='widget-content'>
                <ul id='nav1'>
                  <b:loop values='data:links' var='link'>
                    <li><a expr:href='data:link.target'><data:link.name/></a></li>
                  </b:loop>
                </ul> 
              </div>
            </b:includable>
          </b:widget>
        </b:section>
      </div>
      <!-- Top Social --> 
      <div class='social-area'>
        <b:section class='social-top' id='social-top' maxwidgets='1' name='Social Top' showaddelement='yes'>
          <b:widget id='LinkList50' locked='true' title='Social Media Icons' type='LinkList' version='1'>
            <b:widget-settings>
              <b:widget-setting name='shownum'>2</b:widget-setting>
              <b:widget-setting name='sorting'>NONE</b:widget-setting>
              <b:widget-setting name='text-1'>instagram</b:widget-setting>
              <b:widget-setting name='link-1'>https://instagram.com/patilancha_ladka_ganesh?igshid=ZDc4ODBmNjlmNQ==</b:widget-setting>
              <b:widget-setting name='text-0'>facebook</b:widget-setting>
              <b:widget-setting name='link-0'><![CDATA[https://www.facebook.com/profile.php?id=100012722713929&mibextid=D4KYlr]]></b:widget-setting>
            </b:widget-settings>
            <b:includable id='main'>
              <div class='widget-content'>
                <ul>
                  <b:loop values='data:links' var='link'>
                    <li><a expr:class='data:link.name' expr:href='data:link.target' expr:title='data:link.name' target='_blank'/></li>
                  </b:loop>
                </ul>
              </div>
            </b:includable>
          </b:widget>
        </b:section>
      </div>
    </div>
  </div>
  <div id='header-blog'>
    <div class='header-content row'>
      <div class='header-logo'>
        <b:section id='header' maxwidgets='1' name='Logo' showaddelement='yes'>
          <b:widget id='Header1' locked='true' title='Health with Ganesh  (Header)' type='Header' version='1'>
            <b:widget-settings>
              <b:widget-setting name='displayUrl'>https://blogger.googleusercontent.com/img/a/AVvXsEiJwscVzRfTkYxFV_pSdyLo82qK0_RR4pfxV51b5bTcylAb2uq5w_KLaEOLu82SyuO7va5UnsJ7zA_Cf8kjgglBiKa8STADBMd2c_KuNuTyD2Htc4FtjRW_Auprxdl7r0HCl1WnRrAPko9MhbeSiGpZdhSxMqWZZowAwOtVyahwpVxc54yQWFtwq7-6YmyO=s283</b:widget-setting>
              <b:widget-setting name='displayHeight'>37</b:widget-setting>
              <b:widget-setting name='sectionWidth'>285</b:widget-setting>
              <b:widget-setting name='useImage'>true</b:widget-setting>
              <b:widget-setting name='shrinkToFit'>true</b:widget-setting>
              <b:widget-setting name='imagePlacement'>REPLACE</b:widget-setting>
              <b:widget-setting name='displayWidth'>283</b:widget-setting>
            </b:widget-settings>
            <b:includable id='main'>

              <b:if cond='data:useImage'>
                <b:if cond='data:imagePlacement == &quot;BEHIND&quot;'>
                  <!--
Show image as background to text. You can't really calculate the width
reliably in JS because margins are not taken into account by any of
clientWidth, offsetWidth or scrollWidth, so we don't force a minimum
width if the user is using shrink to fit.
This results in a margin-width's worth of pixels being cropped. If the
user is not using shrink to fit then we expand the header.
-->
                  <b:if cond='data:mobile'>
                    <div id='header-inner'>
                      <div class='titlewrapper' style='background: transparent'>
                        <h1 class='title' style='background: transparent; border-width: 0px'>
                          <b:include name='title'/>
                        </h1>
                      </div>
                      <b:include name='description'/>
                    </div>
                    <b:else/>
                    <div expr:style='&quot;background-image: url(\&quot;&quot; + data:sourceUrl + &quot;\&quot;); &quot;                      + &quot;background-position: &quot;                      + data:backgroundPositionStyleStr + &quot;; &quot;                      + data:widthStyleStr                      + &quot;min-height: &quot; + data:height                      + &quot;_height: &quot; + data:height                      + &quot;background-repeat: no-repeat; &quot;' id='header-inner'>
                      <div class='titlewrapper' style='background: transparent'>
                        <h1 class='title' style='background: transparent; border-width: 0px'>
                          <b:include name='title'/>
                        </h1>
                      </div>
                      <b:include name='description'/>
                    </div>
                  </b:if>
                  <b:else/>
                  <!--Show the image only-->
                  <div id='header-inner'>
                    <a expr:href='data:blog.homepageUrl' style='display: block'><h1 style='display:none;'/>
                      <img expr:alt='data:title' expr:height='data:height' expr:id='data:widget.instanceId + &quot;_headerimg&quot;' expr:src='data:sourceUrl' expr:width='data:width' style='display: block'/>
                    </a>
                    <!--Show the description-->
                    <b:if cond='data:imagePlacement == &quot;BEFORE_DESCRIPTION&quot;'>
                      <b:include name='description'/>
                    </b:if>
                  </div>
                </b:if>
                <b:else/>
                <!--No header image -->
                <div id='header-inner'>
                  <div class='titlewrapper'>
                    <h1 class='title'>
                      <b:include name='title'/>
                    </h1>
                  </div>
                  <b:include name='description'/>
                </div>
              </b:if>
            </b:includable>
            <b:includable id='description'>
              <div class='descriptionwrapper'>
                <p class='description'><span><data:description/></span></p>
              </div>
            </b:includable>
            <b:includable id='title'>
              <b:if cond='data:blog.url == data:blog.homepageUrl'>
                <data:title/>
                <b:else/>
                <a expr:href='data:blog.homepageUrl'><data:title/></a>
              </b:if>
            </b:includable>
          </b:widget>
        </b:section>
      </div>
      <div class='header-ads'>
        <b:section id='ads-content' maxwidgets='1' name='Ads 728x90' showaddelement='yes'/>
      </div>
    </div>
  </div>

  <!-- Main Menu -->
  <nav id='main-nav'>
    <div class='header-menu row'>
      <li class='li-home'><a expr:href='data:blog.homepageUrl'>Home</a></li>
      <b:section id='menu' maxwidgets='1' name='Main Menu' showaddelement='yes'>
        <b:widget id='LinkList98' locked='true' title='' type='LinkList' version='1'>
          <b:includable id='main'>
            <div class='widget-content'>
              <ul class='menu' id='menu-main-nav' itemscope='' itemtype='http://schema.org/SiteNavigationElement'> 
                <b:loop values='data:links' var='link'>
                  <li itemprop='name'><a expr:href='data:link.target' itemprop='url'><data:link.name/></a></li>
                </b:loop>
              </ul>
            </div>
          </b:includable>
        </b:widget>
      </b:section>
      <span id='search-icon'><i class='fa fa-search'/></span>
      <div id='nav-search'>
        <form action='/search' id='searchform' method='get'>
          <input id='s' name='q' placeholder='Type and hit enter to search...' type='text'/>
        </form>
      </div>
    </div>
  </nav>
  <!-- Main Menu (end) -->

  <div class='clear'/>



&lt;div id=&quot;outer-wrapper&quot; class=&quot;<data:blog.pageType/><b:if cond='data:blog.url == data:blog.homepageUrl'> home</b:if><b:if cond='data:blog.pageType == &quot;static_page&quot;'> item</b:if><b:if cond='data:blog.pageType == &quot;archive&quot;'> index</b:if>&quot;&gt;

  <b:if cond='data:blog.canonicalUrl == data:blog.canonicalHomepageUrl'> 
    <!-- featured Posts -->
    <div class='featured row' id='featured'>
      <b:section class='featured-sec' id='featured-sec' maxwidgets='1' name='Featured Posts' showaddelement='yes'>
        <b:widget id='HTML2' locked='false' title='Comments' type='HTML' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<span id=””></span>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
      </b:section>
     
    </div>
  </b:if>

  <div class='clear'/>

    <div class='row' id='content-wrapper'>
      <div class='clear'/>
      <b:if cond='data:blog.pageType == &quot;error_page&quot;'>
      <div id='error-wrap'>
          <h1 class='error-item'>404</h1>
          <h2>Page Not Found!</h2>
          <p>Sorry, the page you were looking for in this blog does not exist.</p>
          <div class='clear'/>
        <a class='homepage' expr:href='data:blog.homepageUrl'><i class='fa fa-home'/> Go To Home</a>
      </div>
      </b:if>

    <div id='main-wrapper'>
   <b:if cond='data:blog.canonicalUrl == data:blog.canonicalHomepageUrl'> 
   <div class='recent-boxes' id='recent-boxes'> 
     <b:section class='box-sec' id='box-sec' name='Box Layout' showaddelement='yes'>
        <b:widget id='BlogSearch1' locked='false' title='Search This Blog' type='BlogSearch' version='2' visible='true'>
          <b:includable id='main'>
    <!-- only display title if it's non-empty -->
    <b:if cond='data:title != &quot;&quot;'>
      <h2 class='title'><data:title/></h2>
    </b:if>

    <div class='widget-content'>
      <div expr:id='data:widget.instanceId + &quot;_form&quot;'>
        <form class='gsc-search-box' expr:action='data:blog.searchUrl'>
          <b:attr cond='not data:view.isPreview' name='target' value='_top'/>
          <table cellpadding='0' cellspacing='0' class='gsc-search-box'>
            <tbody>
              <tr>
                <td class='gsc-input'>
                  <input autocomplete='off' class='gsc-input' expr:value='data:view.isSearch ? data:view.search.query.escaped : &quot;&quot;' name='q' size='10' title='search' type='text'/>
                </td>
                <td class='gsc-search-button'>
                  <input class='gsc-search-button' expr:value='data:messages.search' title='search' type='submit'/>
                </td>
              </tr>
            </tbody>
          </table>
        </form>
      </div>
    </div>

    <b:include name='quickedit'/>
  </b:includable>
          <b:includable id='content'>
  <div class='widget-content' role='search'>
    <b:include name='searchForm'/>
  </div>
</b:includable>
          <b:includable id='searchForm'>
  <form expr:action='data:blog.searchUrl'>
    <b:attr cond='not data:view.isPreview' name='target' value='_top'/>
    <b:include name='urlParamsAsFormInput'/>
    <div class='search-input'>
      <input autocomplete='off' expr:aria-label='data:messages.searchThisBlog' expr:placeholder='data:messages.searchThisBlog' expr:value='data:view.isSearch ? data:view.search.query.escaped : &quot;&quot;' name='q'/>
    </div>
    <b:include name='searchSubmit'/>
  </form>
</b:includable>
          <b:includable id='searchSubmit'>
  <input class='search-action' expr:value='data:messages.search.escaped' type='submit'/>
</b:includable>
        </b:widget>
        <b:widget id='HTML3' locked='false' title='Football' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<span data-label="Football" id="box"></span>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='HTML1' locked='false' title='' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<span id="randomposts"></span>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='PopularPosts1' locked='false' title='Popular Posts' type='PopularPosts' version='1'>
          <b:widget-settings>
            <b:widget-setting name='numItemsToShow'>10</b:widget-setting>
            <b:widget-setting name='showThumbnails'>true</b:widget-setting>
            <b:widget-setting name='showSnippets'>true</b:widget-setting>
            <b:widget-setting name='timeRange'>ALL_TIME</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
           <b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
           <div class='widget-content popular-posts'>
             <ul>
               <b:loop values='data:posts' var='post'>
                 <li>
                   <b:if cond='!data:showThumbnails'>
                     <b:if cond='!data:showSnippets'>
                       <!-- (1) No snippet/thumbnail -->
                       <a expr:href='data:post.href'><data:post.title/></a>
                       <b:else/>
                       <!-- (2) Show only snippets -->
                       <div class='item-title'><a expr:href='data:post.href'><data:post.title/></a></div>
                       <div class='item-snippet'><data:post.snippet/></div>
                     </b:if>
                     <b:else/>
                     <!-- (3) Show only thumbnails or (4) Snippets and thumbnails. -->
                     <div expr:class='data:showSnippets ? &quot;item-content&quot; : &quot;item-thumbnail-only&quot;'>
                       <b:if cond='data:post.thumbnail'>
                         <div class='item-thumbnail'>
                           <a expr:href='data:post.href' target='_blank'>
                             <img border='0' expr:alt='data:post.title' expr:height='data:thumbnailSize' expr:src='data:post.thumbnail' expr:width='data:thumbnailSize'/>
                           </a>
                         </div>
                       </b:if>
                       <div class='item-title'><a expr:href='data:post.href'><data:post.title/></a></div>
                       <b:if cond='data:showSnippets'>
                         <div class='item-snippet'><data:post.snippet/></div>
                       </b:if>
                     </div>
                     <div style='clear: both;'/>
                   </b:if>
                 </li>
               </b:loop>
             </ul>
             <b:include name='quickedit'/>
           </div>
         </b:includable>
        </b:widget>
        <b:widget id='HTML4' locked='false' title='Basketball' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<span data-label="Basketball" id="carousel"></span>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='ReportAbuse1' locked='false' title='' type='ReportAbuse' visible='false'>
          <b:includable id='main'>
  <b:include name='reportAbuse'/>
</b:includable>
        </b:widget>
        <b:widget id='LinkList25' locked='false' title='Variables / Comments' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-1'>commentsSystem</b:widget-setting>
            <b:widget-setting name='link-1'>blogger</b:widget-setting>
            <b:widget-setting name='text-0'>disqusShortname</b:widget-setting>
            <b:widget-setting name='link-2'>//3.bp.blogspot.com/-Yw8BIuvwoSQ/VsjkCIMoltI/AAAAAAAAC4c/s55PW6xEKn0/s1600-r/nth.png</b:widget-setting>
            <b:widget-setting name='link-0'>pikitemplates</b:widget-setting>
            <b:widget-setting name='text-2'>noThumb</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
          <b:include name='content'/>
        </b:includable>
          <b:includable id='content'>
          &lt;script type=&#39;text/javascript&#39;&gt;
          //&lt;![CDATA[
          <b:loop values='data:links' var='link'>
            <b:if cond='data:link.name == &quot;noThumb&quot;'>
              var noThumb = &quot;<data:link.target/>&quot;;
            </b:if>
            <b:if cond='data:link.name == &quot;commentsSystem&quot;'>
              var commentsSystem = &quot;<data:link.target/>&quot;;
            </b:if>
            <b:if cond='data:link.name == &quot;disqusShortname&quot;'>
              var disqusShortname = &quot;<data:link.target/>&quot;;
            </b:if>
          </b:loop>
          //]]&gt;
          &lt;/script&gt;
        </b:includable>
        </b:widget>
        <b:widget id='LinkList27' locked='false' title='Lazy Scrolls / More Text' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-1'>fixedMenu</b:widget-setting>
            <b:widget-setting name='link-1'>true</b:widget-setting>
            <b:widget-setting name='text-0'>fixedSidebar</b:widget-setting>
            <b:widget-setting name='link-2'>Show More</b:widget-setting>
            <b:widget-setting name='link-0'>true</b:widget-setting>
            <b:widget-setting name='text-2'>showMoreText</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
          <b:include name='content'/>
        </b:includable>
          <b:includable id='content'>
          &lt;script type=&#39;text/javascript&#39;&gt;
          //&lt;![CDATA[
          <b:loop values='data:links' var='link'>
            <b:if cond='data:link.name == &quot;fixedSidebar&quot;'>
              var fixedSidebar = <data:link.target/>;
            </b:if>
            <b:if cond='data:link.name == &quot;fixedMenu&quot;'>
              var fixedMenu = <data:link.target/>;
            </b:if>
            <b:if cond='data:link.name == &quot;showMoreText&quot;'>
              var showMoreText = &quot;<data:link.target/>&quot;;
            </b:if>
          </b:loop>
          //]]&gt;
          &lt;/script&gt;
        </b:includable>
        </b:widget>
        <b:widget id='LinkList26' locked='false' title='Related Post / Email Box' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='link-3'>Load More</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-1'>relatedPostsText</b:widget-setting>
            <b:widget-setting name='link-1'>You May Like</b:widget-setting>
            <b:widget-setting name='text-0'>followByEmailText</b:widget-setting>
            <b:widget-setting name='link-2'>3</b:widget-setting>
            <b:widget-setting name='text-3'>loadMorePosts</b:widget-setting>
            <b:widget-setting name='link-0'>Get Notified About Next Update.</b:widget-setting>
            <b:widget-setting name='text-2'>relatedPostsNum</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
          <b:include name='content'/>
        </b:includable>
          <b:includable id='content'>
          &lt;script type=&#39;text/javascript&#39;&gt;
          //&lt;![CDATA[
          <b:loop values='data:links' var='link'>
            <b:if cond='data:link.name == &quot;relatedPostsNum&quot;'>
              var relatedPostsNum = <data:link.target/>;
            </b:if>
             <b:if cond='data:link.name == &quot;followByEmailText&quot;'>
              var followByEmailText = &quot;<data:link.target/>&quot;;
            </b:if>
            <b:if cond='data:link.name == &quot;relatedPostsText&quot;'>
              var relatedPostsText = &quot;<data:link.target/>&quot;;
            </b:if>
            <b:if cond='data:link.name == &quot;loadMorePosts&quot;'>
              var loadMorePosts = &quot;<data:link.target/>&quot;;
            </b:if>
          </b:loop>
          //]]&gt;
          &lt;/script&gt;
        </b:includable>
        </b:widget>
        <b:widget id='FeaturedPost1' locked='false' title='Featured Post' type='FeaturedPost' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='showSnippet'>true</b:widget-setting>
            <b:widget-setting name='showPostTitle'>true</b:widget-setting>
            <b:widget-setting name='postId'>1510665550631527264</b:widget-setting>
            <b:widget-setting name='showFirstImage'>true</b:widget-setting>
            <b:widget-setting name='useMostRecentPost'>false</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- Only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <b:include name='content'/>

  <b:include name='quickedit'/>
</b:includable>
          <b:includable id='content'>
  <div class='post-summary'>
    <b:if cond='data:showPostTitle and data:postTitle != &quot;&quot;'>
      <h3><a expr:href='data:postUrl'><data:postTitle/></a></h3>
    </b:if>
    <b:if cond='data:showSnippet and data:postSummary != &quot;&quot;'>
      <p>
        <data:postSummary/>
      </p>
    </b:if>
    <b:if cond='data:showFirstImage and data:postFirstImage != &quot;&quot;'>
      <img class='image' expr:src='data:postFirstImage'/>
    </b:if>
  </div>

  <style type='text/css'>
    .image {
      width: 100%;
    }
  </style>
</b:includable>
        </b:widget>
        <b:widget id='HTML10' locked='false' title='Technology' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'>3/Technology/post-list</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='HTML13' locked='false' title='Top Videos' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'>megagrid/recent</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='HTML14' locked='false' title='' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<a class='piki-ads' href="javascript:;">Your Responsive Ads code (Google Ads)</a>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='HTML15' locked='false' title='' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<a class='piki-ads' href="javascript:;">Your Responsive Ads code (Google Ads)</a>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='HTML18' locked='false' title='Trending Weekly' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'>4/sgrid/recent</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='LinkList76' locked='false' title='Social Plugin' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='link-7'>#</b:widget-setting>
            <b:widget-setting name='link-5'>#</b:widget-setting>
            <b:widget-setting name='link-6'>#</b:widget-setting>
            <b:widget-setting name='link-3'>#</b:widget-setting>
            <b:widget-setting name='link-4'>#</b:widget-setting>
            <b:widget-setting name='text-1'>twitter</b:widget-setting>
            <b:widget-setting name='text-0'>facebook</b:widget-setting>
            <b:widget-setting name='text-3'>reddit</b:widget-setting>
            <b:widget-setting name='text-2'>whatsapp</b:widget-setting>
            <b:widget-setting name='text-5'>vk</b:widget-setting>
            <b:widget-setting name='text-4'>pinterest</b:widget-setting>
            <b:widget-setting name='text-7'>youtube</b:widget-setting>
            <b:widget-setting name='text-6'>instagram</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='link-1'>#</b:widget-setting>
            <b:widget-setting name='link-2'>#</b:widget-setting>
            <b:widget-setting name='link-0'>http://fb.com/pikitemplates</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <b:include name='widget-title'/>
  <b:include name='content'/>
</b:includable>
          <b:includable id='content'>
              <div class='widget-content'>
                <ul class='socialFilter social-bg social'>
                  <b:loop values='data:links' var='link'>
                   <li>
                    <a expr:class='data:link.name' expr:href='data:link.target' expr:title='data:link.name' rel='noopener noreferrer' target='_blank'>
                    <data:link.name/>
                    </a>
                    </li>
                    </b:loop>
                </ul>
              </div>
            </b:includable>
        </b:widget>
        <b:widget id='TextList15' locked='false' title='Facebook SDK (Plugin)' type='TextList' visible='true'>
          <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <b:include name='content'/>
    </b:includable>
          <b:includable id='content'>
      <b:include name='textlist-content'/>
    </b:includable>
        </b:widget>
        <b:widget id='HTML42' locked='false' title='Top Stories' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'/>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='LinkList1' locked='false' title='Css Options' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-1'>recentPostsHeadline</b:widget-setting>
            <b:widget-setting name='link-1'>true</b:widget-setting>
            <b:widget-setting name='text-0'>boxedVersion</b:widget-setting>
            <b:widget-setting name='link-0'>false</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>

<b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
   <b:include name='quickedit'/>
 </div>
</b:includable>
          <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
        </b:widget>
        <b:widget id='HTML43' locked='false' title='What&apos;s New' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'>block/recent</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='LinkList2' locked='false' title='Default Variables' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='link-3'>5</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-1'>commentsSystem</b:widget-setting>
            <b:widget-setting name='link-1'>blogger</b:widget-setting>
            <b:widget-setting name='text-0'>disqusShortname</b:widget-setting>
            <b:widget-setting name='link-2'>true</b:widget-setting>
            <b:widget-setting name='text-3'>postPerPage</b:widget-setting>
            <b:widget-setting name='link-0'>soratemplates</b:widget-setting>
            <b:widget-setting name='text-2'>fixedSidebar</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>

<b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
   <b:include name='quickedit'/>
 </div>
</b:includable>
          <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
        </b:widget>
        <b:widget id='LinkList4' locked='false' title='top social' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='link-3'>https://twitter.com/PikiTemplates</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='link-4'>https://www.instagram.com/pikitemplates</b:widget-setting>
            <b:widget-setting name='text-1'>whatsapp</b:widget-setting>
            <b:widget-setting name='link-1'>#</b:widget-setting>
            <b:widget-setting name='text-0'>facebook</b:widget-setting>
            <b:widget-setting name='link-2'>#</b:widget-setting>
            <b:widget-setting name='text-3'>twitter</b:widget-setting>
            <b:widget-setting name='link-0'>https://facebook.com/pikitemplates</b:widget-setting>
            <b:widget-setting name='text-2'>telegram</b:widget-setting>
            <b:widget-setting name='text-4'>instagram</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
          <b:includable id='content'>
                      <div class='widget-content'>
                        <ul class='social'>
                          <b:loop values='data:links' var='link'>
                         <li><a expr:class='data:link.name' expr:href='data:link.target' rel='noopener noreferrer' target='_blank'/></li>
                          </b:loop>
                        </ul>
                      </div>
                    </b:includable>
        </b:widget>
        <b:widget id='LinkList5' locked='false' title='Link List' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='link-3'>https://www.healthwithganesh.com/p/terms-and-conditions.html</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='link-4'>https://www.healthwithganesh.com/p/privacy-policy.html</b:widget-setting>
            <b:widget-setting name='text-1'>Contacts Us</b:widget-setting>
            <b:widget-setting name='link-1'>https://www.healthwithganesh.com/p/contacts-us.html</b:widget-setting>
            <b:widget-setting name='text-0'>About Us</b:widget-setting>
            <b:widget-setting name='link-2'>https://www.healthwithganesh.com/p/disclaimer.html</b:widget-setting>
            <b:widget-setting name='text-3'>Terms and Conditions</b:widget-setting>
            <b:widget-setting name='link-0'>https://www.healthwithganesh.com/p/about-us.html</b:widget-setting>
            <b:widget-setting name='text-2'>Disclaimer</b:widget-setting>
            <b:widget-setting name='text-4'>Privacy Policy</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>

<b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
   <b:include name='quickedit'/>
 </div>
</b:includable>
          <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
        </b:widget>
        <b:widget id='LinkList6' locked='false' title='Css Options' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-1'>recentPostsHeadline</b:widget-setting>
            <b:widget-setting name='link-1'>true</b:widget-setting>
            <b:widget-setting name='text-0'>boxedVersion</b:widget-setting>
            <b:widget-setting name='link-0'>false</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>

<b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
   <b:include name='quickedit'/>
 </div>
</b:includable>
          <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
        </b:widget>
        <b:widget id='LinkList7' locked='false' title='Follow Us' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-1'>youtube</b:widget-setting>
            <b:widget-setting name='link-1'>https://www.youtube.com/@Ganeshpatil-lo5wj</b:widget-setting>
            <b:widget-setting name='text-0'>facebook-f</b:widget-setting>
            <b:widget-setting name='link-2'>https://www.instagram.com/patilancha_ladka_ganesh/?igshid=ZDc4ODBmNjlmNQ%3D%3D</b:widget-setting>
            <b:widget-setting name='link-0'><![CDATA[https://www.facebook.com/profile.php?id=100012722713929&mibextid=D4KYlr]]></b:widget-setting>
            <b:widget-setting name='text-2'>instagram</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
            <b:include name='content'/>
          </b:includable>
          <b:includable id='content'>
            <div class='widget-content'>
              <b:include name='widget-title'/>
              <ul class='social-footer social-bg'>
                <b:loop values='data:links' var='link'>
                  <li expr:class='data:link.name'><a expr:class='data:link.name' expr:href='data:link.target' rel='noopener noreferrer' target='_blank'/></li>
                </b:loop>
              </ul>
            </div>
          </b:includable>
        </b:widget>
        <b:widget id='Profile1' locked='false' title='About Me' type='Profile' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='showaboutme'>true</b:widget-setting>
            <b:widget-setting name='showlocation'>false</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
    <b:if cond='data:title != &quot;&quot;'>
      <h2><data:title/></h2>
    </b:if>
    <div class='widget-content'>
    <b:if cond='data:team'> <!-- team blog profile -->
      <ul>
        <b:loop values='data:authors' var='i'>
          <li><a class='profile-name-link g-profile' expr:href='data:i.userUrl' expr:style='&quot;background-image: url(&quot; + data:i.profileLogo + &quot;);&quot;'><data:i.display-name/></a></li>
        </b:loop>
      </ul>

    <b:else/> <!-- normal blog profile -->

      <b:if cond='data:photo.url != &quot;&quot;'>
        <a expr:href='data:userUrl'><img class='profile-img' expr:alt='data:messages.myPhoto' expr:height='data:photo.height' expr:src='data:photo.url' expr:width='data:photo.width'/></a>
      </b:if>

      <dl class='profile-datablock'>
        <dt class='profile-data'>
          <a class='profile-name-link g-profile' expr:href='data:userUrl' expr:style='&quot;background-image: url(&quot; + data:profileLogo + &quot;);&quot;' rel='author'>
            <data:displayname/>
          </a>
        </dt>

        <b:if cond='data:showlocation'>
          <dd class='profile-data'><data:location/></dd>
        </b:if>

        <b:if cond='data:aboutme != &quot;&quot;'><dd class='profile-textblock'><data:aboutme/></dd></b:if>
      </dl>
      <a class='profile-link' expr:href='data:userUrl' rel='author'><data:viewProfileMsg/></a>
    </b:if>

     <b:include name='quickedit'/>
    </div>
  </b:includable>
          <b:includable id='authorProfileImage'>
  <img class='profile-img' expr:alt='data:messages.myPhoto' expr:height='data:authorPhoto.height' expr:src='data:authorPhoto.image' expr:width='data:authorPhoto.width'/>
</b:includable>
          <b:includable id='content'>
  <b:if cond='data:team'>
    <div class='widget-content team'>
      <b:include name='teamProfile'/>
    </div>
  <b:else/>
    <div class='widget-content individual'>
      <b:include name='userProfile'/>
    </div>
  </b:if>
</b:includable>
          <b:includable id='defaultProfileImage'>
  <div class='default-avatar'/>
</b:includable>
          <b:includable id='profileImage'>
  <b:if cond='data:authorPhoto.image'>
    <b:include name='authorProfileImage'/>
  <b:else/>
    <b:include name='defaultProfileImage'/>
  </b:if>
</b:includable>
          <b:includable id='teamProfile'>
  <ul>
    <b:loop values='data:authors' var='author'>
      <li>
        <div class='team-member'>
          <b:include data='author' name='teamProfileLink'/>
        </div>
      </li>
    </b:loop>
  </ul>
</b:includable>
          <b:includable id='teamProfileLink'>
  <a class='profile-link g-profile' expr:href='data:userUrl' rel='nofollow'>
    <b:include name='profileImage'/>
    <span class='profile-name'><data:display-name/></span>
  </a>
</b:includable>
          <b:includable id='userLocation'>
  <dd class='profile-data location'><data:location/></dd>
</b:includable>
          <b:includable id='userProfile'>
  <b:include name='userProfileImage'/>
  <b:include name='userProfileInfo'/>
</b:includable>
          <b:includable id='userProfileData'>
  <dt class='profile-data'>
    <a class='profile-link g-profile' expr:href='data:userUrl' rel='author nofollow'>
      <data:displayname/>
    </a>
  </dt>
</b:includable>
          <b:includable id='userProfileImage'>
  <a expr:href='data:userUrl' rel='nofollow'>
    <b:include name='profileImage'/>
  </a>
</b:includable>
          <b:includable id='userProfileInfo'>
  <div class='profile-info'>
    <dl class='profile-datablock'>
      <b:class cond='data:showlocation and data:location != &quot;&quot;' name='has-location'/>

      <b:include name='userProfileData'/>
      <b:include cond='data:showlocation and data:location != &quot;&quot;' name='userLocation'/>
      <b:include cond='data:aboutme != &quot;&quot;' name='userProfileText'/>
    </dl>
    <b:include name='viewProfileLink'/>
  </div>
</b:includable>
          <b:includable id='userProfileText'>
  <dd class='profile-textblock'>
    <data:aboutme/>
  </dd>
</b:includable>
          <b:includable id='viewProfileLink'>
  <a class='profile-link' expr:href='data:userUrl' rel='author nofollow'>
    <data:messages.viewMyCompleteProfile/>
  </a>
</b:includable>
        </b:widget>
        <b:widget id='ContactForm1' locked='false' title='Contact form' type='ContactForm' version='2' visible='false'>
          <b:includable id='main'>
          <b:include name='widget-title'/>
          <b:include name='content'/>
        </b:includable>
          <b:includable id='content'>
          <div class='contact-form-widget'>
            <div class='form'>
              <form name='contact-form'>
                <input class='contact-form-name' expr:id='data:widget.instanceId + &quot;_contact-form-name&quot;' expr:placeholder='data:contactFormNameMsg' name='name' size='30' type='text' value=''/>
                <input class='contact-form-email' expr:id='data:widget.instanceId + &quot;_contact-form-email&quot;' expr:placeholder='data:contactFormEmailMsg + &quot;*&quot;' name='email' size='30' type='text' value=''/>
                <textarea class='contact-form-email-message' cols='25' expr:id='data:widget.instanceId + &quot;_contact-form-email-message&quot;' expr:placeholder='data:contactFormMessageMsg + &quot;*&quot;' name='email-message' rows='5'/>
                <input class='contact-form-button contact-form-button-submit' expr:id='data:widget.instanceId + &quot;_contact-form-submit&quot;' expr:value='data:contactFormSendMsg' type='button'/>
                <p class='contact-form-error-message' expr:id='data:widget.instanceId + &quot;_contact-form-error-message&quot;'/>
                <p class='contact-form-success-message' expr:id='data:widget.instanceId + &quot;_contact-form-success-message&quot;'/>
              </form>
            </div>
          </div>
        </b:includable>
        </b:widget>
        <b:widget id='AdSense1' locked='false' title='' type='AdSense' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='style.bgcolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.textcolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.layout'>1x1</b:widget-setting>
            <b:widget-setting name='style.bordercolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.urlcolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.linkcolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.unittype'>TextAndImage</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <div class='widget-content'>
    <data:adCode/>
    <b:include name='quickedit'/>
  </div>
</b:includable>
        </b:widget>
        <b:widget id='AdSense2' locked='false' title='' type='AdSense' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='style.bgcolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.textcolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.layout'>1x1</b:widget-setting>
            <b:widget-setting name='style.bordercolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.urlcolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.linkcolor'>#ffffff</b:widget-setting>
            <b:widget-setting name='style.unittype'>TextAndImage</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <div class='widget-content'>
    <data:adCode/>
    <b:include name='quickedit'/>
  </div>
</b:includable>
        </b:widget>
        <b:widget id='Image2' locked='false' title='Mobile Logo Settings' type='Image' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='displayUrl'>http://3.bp.blogspot.com/-SPv_Vor-GI0/W1lWtiLlg-I/AAAAAAAACnw/82Tzze3hkdgTlUvklRq1LEbvSklN_KZQACK4BGAYYCw/s159/logo_mobile.png</b:widget-setting>
            <b:widget-setting name='displayHeight'>33</b:widget-setting>
            <b:widget-setting name='sectionWidth'>150</b:widget-setting>
            <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
            <b:widget-setting name='displayWidth'>159</b:widget-setting>
            <b:widget-setting name='link'>My Title</b:widget-setting>
            <b:widget-setting name='caption'>image</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
    <b:if cond='data:title != &quot;&quot;'>
      <h2><data:title/></h2>
    </b:if>
    <div class='widget-content'>
      <b:tag cond='data:link' expr:href='data:link' name='a'>
        <img expr:alt='data:title' expr:height='data:height' expr:id='data:widget.instanceId + &quot;_img&quot;' expr:src='data:sourceUrl' expr:width='data:width'/>
      </b:tag>
      <br/>
      <b:if cond='data:caption'>
        <span class='caption'><data:caption/></span>
      </b:if>
    </div>
    <b:include name='quickedit'/>
  </b:includable>
          <b:includable id='content'>
  <div class='widget-content'>
    <b:tag cond='data:link' expr:href='data:link' name='a'>
      <img expr:alt='data:title' expr:height='data:height' expr:id='data:widget.instanceId + &quot;_img&quot;' expr:src='data:sourceUrl' expr:width='data:width'>
        <b:attr cond='data:sourceSet' expr:value='data:sourceSet' name='srcset'/>
      </img>
    </b:tag>
    <br/>
    <b:if cond='data:caption'>
      <span class='caption'><data:caption/></span>
    </b:if>
  </div>
</b:includable>
        </b:widget>
        <b:widget id='Image1' locked='false' title='Mobile Logo Settings' type='Image' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='displayUrl'>http://3.bp.blogspot.com/-SPv_Vor-GI0/W1lWtiLlg-I/AAAAAAAACnw/82Tzze3hkdgTlUvklRq1LEbvSklN_KZQACK4BGAYYCw/s159/logo_mobile.png</b:widget-setting>
            <b:widget-setting name='displayHeight'>33</b:widget-setting>
            <b:widget-setting name='sectionWidth'>150</b:widget-setting>
            <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
            <b:widget-setting name='displayWidth'>159</b:widget-setting>
            <b:widget-setting name='link'>My Title</b:widget-setting>
            <b:widget-setting name='caption'>image</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
    <b:if cond='data:title != &quot;&quot;'>
      <h2><data:title/></h2>
    </b:if>
    <div class='widget-content'>
      <b:tag cond='data:link' expr:href='data:link' name='a'>
        <img expr:alt='data:title' expr:height='data:height' expr:id='data:widget.instanceId + &quot;_img&quot;' expr:src='data:sourceUrl' expr:width='data:width'/>
      </b:tag>
      <br/>
      <b:if cond='data:caption'>
        <span class='caption'><data:caption/></span>
      </b:if>
    </div>
    <b:include name='quickedit'/>
  </b:includable>
          <b:includable id='content'>
  <div class='widget-content'>
    <b:tag cond='data:link' expr:href='data:link' name='a'>
      <img expr:alt='data:title' expr:height='data:height' expr:id='data:widget.instanceId + &quot;_img&quot;' expr:src='data:sourceUrl' expr:width='data:width'>
        <b:attr cond='data:sourceSet' expr:value='data:sourceSet' name='srcset'/>
      </img>
    </b:tag>
    <br/>
    <b:if cond='data:caption'>
      <span class='caption'><data:caption/></span>
    </b:if>
  </div>
</b:includable>
        </b:widget>
        <b:widget id='Label2' locked='false' title='Labels' type='Label' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>ALPHA</b:widget-setting>
            <b:widget-setting name='display'>CLOUD</b:widget-setting>
            <b:widget-setting name='selectedLabelsList'/>
            <b:widget-setting name='showType'>ALL</b:widget-setting>
            <b:widget-setting name='showFreqNumbers'>true</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <b:include name='content'/>
    </b:includable>
          <b:includable id='cloud'>
  <b:loop values='data:labels' var='label'>
    <span class='label-size'>
      <b:class expr:name='&quot;label-size-&quot; + data:label.cssSize'/>
      <a class='label-name' expr:href='data:label.url'>
        <data:label.name/>
        <b:if cond='data:this.showFreqNumbers'>
          <span class='label-count'><data:label.count/></span>
        </b:if>
      </a>
    </span>
  </b:loop>
</b:includable>
          <b:includable id='content'>
      <div class='widget-content'>
        <b:class expr:name='data:this.display + &quot;-label&quot;'/>
        <b:include cond='data:this.display == &quot;list&quot;' name='list'/>
        <b:include cond='data:this.display == &quot;cloud&quot;' name='list'/>
      </div>
    </b:includable>
          <b:includable id='list'>
      <ul>
        <b:loop values='data:labels' var='label'>
          <li>
            <a class='label-name' expr:href='data:label.url'>
              <data:label.name/>
              <b:if cond='data:this.showFreqNumbers'>
                <span class='label-count'><data:label.count/></span>
              </b:if>
            </a>
          </li>
        </b:loop>
      </ul>
    </b:includable>
        </b:widget>
        <b:widget id='HTML33' locked='false' title='Footer Copyright' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'>&lt;div class=&quot;footer&quot;&gt;
        &lt;p&gt;Copyright &amp;copy; www.healthwithganesh.com&lt;/p&gt;
    &lt;/div&gt;</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
        <b:widget id='Image150' locked='false' title='About Us' type='Image' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='displayUrl'>http://1.bp.blogspot.com/-lI0XT7zKWhQ/YJDTCfytdGI/AAAAAAAABjQ/aWTm9VTsQuMIuQjdVLffH4SUDzDAXE-sACK4BGAYYCw/s294/Galaxy%2BTemplate.png</b:widget-setting>
            <b:widget-setting name='displayHeight'>67</b:widget-setting>
            <b:widget-setting name='sectionWidth'>150</b:widget-setting>
            <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
            <b:widget-setting name='displayWidth'>294</b:widget-setting>
            <b:widget-setting name='link'/>
            <b:widget-setting name='caption'><![CDATA[Health with Ganesh is a websites is to build trust, be an online presence so the interested people can find the required information about health and fitness. Journey of Fitness and Culinary Exploration! Go along with us as we reveal the ideal mix of wellbeing and experience through our blog, where we share master tips on remaining fit while appreciating worldwide cooking styles during your movements. Find tempting recipes, savvy exercise routine schedules, and shrewd travel directs that make health an astonishing piece of your excursions. How about we investigate the world, enjoy flavorful dishes, and focus on our prosperity together."]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main' var='this'>
            <b:include name='content'/>
          </b:includable>
          <b:includable id='content'>
            <div class='widget-content'>
              <b:if cond='data:link == &quot;hide-image&quot;'>
                <b:class name='no-image'/>
              </b:if>
              <b:if cond='data:link != &quot;hide-image&quot;'>
                <div class='footer-logo custom-image'>
                  <a expr:href='data:blog.homepageUrl'>
                    <img expr:alt='data:blog.title' expr:id='data:widget.instanceId + &quot;_img&quot;' expr:src='data:sourceUrl'/>
                  </a>
                </div>
              </b:if>
              <div class='about-content'>
                <b:include name='widget-title'/>
                <b:if cond='data:caption'>
                  <span class='image-caption'><data:caption/></span>
                </b:if>
              </div>
            </div>
          </b:includable>
        </b:widget>
        <b:widget id='LinkList56' locked='false' title='Main Menu' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='text-10'>Documentation</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='link-1'>megamenu/recent</b:widget-setting>
            <b:widget-setting name='link-2'>#</b:widget-setting>
            <b:widget-setting name='link-12'>https://www.pikitemplates.com/2021/05/galaxy-blogger-template.html</b:widget-setting>
            <b:widget-setting name='link-0'>/</b:widget-setting>
            <b:widget-setting name='link-11'>/p/shortcodes.html</b:widget-setting>
            <b:widget-setting name='link-10'>https://blogging.pikitemplates.com/2021/05/documentation-of-galaxy.html</b:widget-setting>
            <b:widget-setting name='text-9'>_Contact us</b:widget-setting>
            <b:widget-setting name='link-9'>#</b:widget-setting>
            <b:widget-setting name='text-8'>_Error Page</b:widget-setting>
            <b:widget-setting name='link-7'>/2020/01/i-will-prepare-and-some-day-my-chance.html</b:widget-setting>
            <b:widget-setting name='link-8'>/pikitemplates</b:widget-setting>
            <b:widget-setting name='link-5'>/2020/01/the-difference-between-winning-and.html</b:widget-setting>
            <b:widget-setting name='link-6'>/2020/01/life-is-fragile-were-not-guaranteed.html</b:widget-setting>
            <b:widget-setting name='link-3'>#</b:widget-setting>
            <b:widget-setting name='link-4'>#</b:widget-setting>
            <b:widget-setting name='text-1'>Mega Menu</b:widget-setting>
            <b:widget-setting name='text-0'>Home</b:widget-setting>
            <b:widget-setting name='text-3'>_Featured Posts</b:widget-setting>
            <b:widget-setting name='text-2'>Features</b:widget-setting>
            <b:widget-setting name='text-5'>__Left Sidebar</b:widget-setting>
            <b:widget-setting name='text-4'>_Post ShortCodes</b:widget-setting>
            <b:widget-setting name='text-7'>__Full Width</b:widget-setting>
            <b:widget-setting name='text-6'>__Right Sidebar</b:widget-setting>
            <b:widget-setting name='text-11'>ShortCodes</b:widget-setting>
            <b:widget-setting name='text-12'>Download this Template</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
                  <b:include name='content'/>
                </b:includable>
          <b:includable id='content'>
                  <ul id='xxqo-menuaflex-list' role='menubar'>
                    <b:loop values='data:links' var='link'>
                      <li itemprop='name'><a expr:href='data:link.target' itemprop='url'><data:link.name/></a></li>
                    </b:loop>
                  </ul>
                </b:includable>
        </b:widget>
        <b:widget id='LinkList12' locked='false' title='Menu Footer Widget' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-1'>About</b:widget-setting>
            <b:widget-setting name='link-1'>https://newsplus-templatesyard.blogspot.com/p/about.html</b:widget-setting>
            <b:widget-setting name='text-0'>Home</b:widget-setting>
            <b:widget-setting name='link-2'>https://newsplus-templatesyard.blogspot.com/p/contact-us.html</b:widget-setting>
            <b:widget-setting name='link-0'>/</b:widget-setting>
            <b:widget-setting name='text-2'>Contact Us</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>

<b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
   <b:include name='quickedit'/>
 </div>
</b:includable>
          <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
        </b:widget>
        <b:widget id='LinkList8' locked='false' title='Link List' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='link-3'>/p/about-us.html</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='link-4'>https://ganeshpatil14.blogspot.com/p/terms-and-conditions.html</b:widget-setting>
            <b:widget-setting name='text-1'>About</b:widget-setting>
            <b:widget-setting name='link-1'>/p/about-us.html</b:widget-setting>
            <b:widget-setting name='text-0'>Home</b:widget-setting>
            <b:widget-setting name='link-2'>/p/about-us.html</b:widget-setting>
            <b:widget-setting name='text-3'>Privacy Policy</b:widget-setting>
            <b:widget-setting name='link-0'>/</b:widget-setting>
            <b:widget-setting name='text-2'>Contact us</b:widget-setting>
            <b:widget-setting name='text-4'>Terms and Conditions</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
          <b:includable id='content'>
              <div class='widget-content'>
                <ul>
                  <b:loop values='data:links' var='link'>
                    <li><a expr:href='data:link.target'><data:link.name/></a></li>
                  </b:loop>
                </ul>
              </div>
            </b:includable>
        </b:widget>
        <b:widget id='LinkList9' locked='false' title='' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-1'>instagram</b:widget-setting>
            <b:widget-setting name='link-1'>patilancha_ladka_prince_ganesh</b:widget-setting>
            <b:widget-setting name='text-0'>facebook</b:widget-setting>
            <b:widget-setting name='link-2'>https://www.youtube.com/@Ganeshpatil-lo5wj</b:widget-setting>
            <b:widget-setting name='link-0'><![CDATA[https://www.facebook.com/profile.php?id=100012722713929&mibextid=D4KYlr]]></b:widget-setting>
            <b:widget-setting name='text-2'>utube</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>

<b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
   <b:include name='quickedit'/>
 </div>
</b:includable>
          <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
        </b:widget>
        <b:widget id='HTML9' locked='false' title='Below Post Ad' type='HTML' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<a class='piki-ads' href="javascript:;">Below Post Responsive Ads code (Google Ads)</a>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <div class='widget-content'>
    <data:content/>
  </div>
</b:includable>
        </b:widget>
        <b:widget id='LinkList13' locked='false' title='Social Plugin' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='text-0'>facebook</b:widget-setting>
            <b:widget-setting name='link-0'><![CDATA[https://www.facebook.com/profile.php?id=100012722713929&mibextid=D4KYlr]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>

<b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
   <b:include name='quickedit'/>
 </div>
</b:includable>
          <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
        </b:widget>
        <b:widget id='PageList1' locked='false' title='' type='PageList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='pageListJson'><![CDATA[{"link0":{"href":"https://www.healthwithganesh.com","position":0,"title":"Home"}}]]></b:widget-setting>
            <b:widget-setting name='homeTitle'>Home</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
  <div class='widget-content'>
    <b:if cond='data:mobile'>
      <select expr:id='data:widget.instanceId + &quot;_select&quot;'>
        <b:if cond='data:showPlaceholder'>
          <option disabled='disabled' hidden='hidden' value=''>
            <b:attr cond='!data:hasCurrentPage' name='selected' value='selected'/>
            <b:message name='messages.moveToPage'/>
          </option>
        </b:if>
        <b:loop values='data:links' var='link'>
          <option expr:value='data:link.href'>
            <b:attr cond='data:link.isCurrentPage' name='selected' value='selected'/>
            <data:link.title/>
          </option>
        </b:loop>
      </select>
      <span class='pagelist-arrow'>&amp;#9660;</span>
    <b:else/>
      <ul>
        <b:loop values='data:links' var='link'>
          <li>
            <b:class cond='data:link.isCurrentPage' name='selected'/>
            <a expr:href='data:link.href'><data:link.title/></a>
          </li>
        </b:loop>
      </ul>
    </b:if>
    <b:include name='quickedit'/>
  </div>
</b:includable>
          <b:includable id='content'>
  <div class='widget-content'>
    <b:include name='pageList'/>
  </div>
</b:includable>
          <b:includable id='overflowButton'>
  <b:include name='verticalMoreIcon'/>
</b:includable>
          <b:includable id='overflowablePageList'>
  <div class='overflowable-container'>
    <div class='overflowable-contents'>
      <div class='container'>
        <b:with value='true' var='overflow'>
        <b:with value='&quot;tabs&quot;' var='pageListClass'>
          <b:include name='pageList'/>
        </b:with>
        </b:with>
      </div>
    </div>
    <div class='overflow-button hidden'>
      <b:include name='overflowButton'/>
    </div>
  </div>
</b:includable>
          <b:includable id='pageLink'>
  <li>
    <b:class cond='data:overflow' name='overflowable-item'/>
    <b:class cond='data:link.isCurrentPage' name='selected'/>

    <a expr:href='data:link.href'><data:link.title/></a>
  </li>
</b:includable>
          <b:includable id='pageList'>
  <ul>
    <b:class cond='data:pageListClass' expr:name='data:pageListClass'/>
    <b:loop values='data:links' var='link'>
      <b:include name='pageLink'/>
    </b:loop>
  </ul>
</b:includable>
        </b:widget>
        <b:widget id='PageList2' locked='false' title='' type='PageList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='pageListJson'><![CDATA[{"link0":{"href":"http://ganeshpatil14.blogspot.com/","position":0,"title":"Home"}}]]></b:widget-setting>
            <b:widget-setting name='homeTitle'>Home</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
  <div class='widget-content'>
    <b:if cond='data:mobile'>
      <select expr:id='data:widget.instanceId + &quot;_select&quot;'>
        <b:if cond='data:showPlaceholder'>
          <option disabled='disabled' hidden='hidden' value=''>
            <b:attr cond='!data:hasCurrentPage' name='selected' value='selected'/>
            <b:message name='messages.moveToPage'/>
          </option>
        </b:if>
        <b:loop values='data:links' var='link'>
          <option expr:value='data:link.href'>
            <b:attr cond='data:link.isCurrentPage' name='selected' value='selected'/>
            <data:link.title/>
          </option>
        </b:loop>
      </select>
      <span class='pagelist-arrow'>&amp;#9660;</span>
    <b:else/>
      <ul>
        <b:loop values='data:links' var='link'>
          <li>
            <b:class cond='data:link.isCurrentPage' name='selected'/>
            <a expr:href='data:link.href'><data:link.title/></a>
          </li>
        </b:loop>
      </ul>
    </b:if>
    <b:include name='quickedit'/>
  </div>
</b:includable>
          <b:includable id='content'>
  <div class='widget-content'>
    <b:include name='pageList'/>
  </div>
</b:includable>
          <b:includable id='overflowButton'>
  <b:include name='verticalMoreIcon'/>
</b:includable>
          <b:includable id='overflowablePageList'>
  <div class='overflowable-container'>
    <div class='overflowable-contents'>
      <div class='container'>
        <b:with value='true' var='overflow'>
        <b:with value='&quot;tabs&quot;' var='pageListClass'>
          <b:include name='pageList'/>
        </b:with>
        </b:with>
      </div>
    </div>
    <div class='overflow-button hidden'>
      <b:include name='overflowButton'/>
    </div>
  </div>
</b:includable>
          <b:includable id='pageLink'>
  <li>
    <b:class cond='data:overflow' name='overflowable-item'/>
    <b:class cond='data:link.isCurrentPage' name='selected'/>

    <a expr:href='data:link.href'><data:link.title/></a>
  </li>
</b:includable>
          <b:includable id='pageList'>
  <ul>
    <b:class cond='data:pageListClass' expr:name='data:pageListClass'/>
    <b:loop values='data:links' var='link'>
      <b:include name='pageLink'/>
    </b:loop>
  </ul>
</b:includable>
        </b:widget>
        <b:widget id='PopularPosts3' locked='false' title='Breaking Ticker' type='PopularPosts' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='numItemsToShow'>10</b:widget-setting>
            <b:widget-setting name='showThumbnails'>true</b:widget-setting>
            <b:widget-setting name='showSnippets'>true</b:widget-setting>
            <b:widget-setting name='timeRange'>LAST_YEAR</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <div class='widget-content'>
        <b:if cond='data:widget.sectionId == &quot;hot-posts&quot;'>
           <div class='xx0xx-bticker'>
              <b:loop index='i' values='data:posts' var='post'>
                <b:include data='post' name='content'/>
              </b:loop>
              </div>
              <div class='mydivs-bt'>
               <a class='prev' href='javascript:;' role='button'/>
              <a class='next' href='javascript:;' role='button'/>
               </div>
          <b:elseif cond='data:widget.sectionId == &quot;ft-post&quot;'/>
          <div class='GalaxyPSpeed-holds'>
            <b:loop index='i' values='data:posts' var='post'>
              <b:include cond='data:i in [0,1,2,3,4]' data='post' name='content'/>
            </b:loop>
          </div>
          <b:else/>
          <b:class name='sidebar-posts'/>
          <b:loop index='i' values='data:posts' var='post'>
            <b:include data='post' name='content'/>
          </b:loop>
        </b:if>
      </div>
    </b:includable>
          <b:includable id='blogThisShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='bylineByName' var='byline'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='bylineRegion' var='regionItems'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='commentsLink'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='commentsLinkIframe'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='content' var='post'>
      <div>
        <b:if cond='data:widget.sectionId == &quot;hot-posts&quot;'>
          <b:class name='GalaxyTicker'/>
          <b:elseif cond='data:widget.sectionId == &quot;ft-post&quot;'/>
          <b:class name='GalaxyPSpeedArea'/>
          <b:else/>
          <b:class expr:name='data:i == 0 ? &quot;popular-post post gaint-post&quot; : &quot;popular-post post&quot;'/>
        </b:if>
        <b:class expr:name='&quot;item&quot;+data:i'/>
          <b:if cond='data:widget.sectionId not in [&quot;hot-posts&quot;]'>
          <a class='post-filter-link background-layer image-nos' expr:href='data:post.url.canonical' expr:title='data:post.title ? data:post.title : data:messages.noTitle'>
          <b:if cond='data:post.featuredImage'>
          <img class='snip-thumbnail' expr:alt='data:post.title ? data:post.title : data:messages.noTitle' expr:src='data:post.featuredImage.isYouTube ? resizeImage(data:post.featuredImage.youtubeMaxResDefaultUrl.jsonEscaped, 680) : resizeImage(data:post.featuredImage, 680)'/>
          <b:else/>
          <img class='snip-thumbnail' expr:alt='data:post.title ? data:post.title : data:messages.noTitle' src='https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png'/>
          </b:if><b:class expr:name='data:post.featuredImage.isYouTube ? &quot;video-nos&quot; : &quot;image-nos&quot;'/>
          </a>
          </b:if>
          <b:if cond='data:widget.sectionId == &quot;ft-post&quot;'>
           <div class='featured-meta'>
          <b:if cond='data:post.labels and ((data:widget.sectionId in [&quot;ft-post&quot;]) or (data:widget.sectionId == &quot;sidebar&quot; and data:i == 0))'><span class='label-news-flex'><data:post.labels.first.name/></span></b:if>
          <h2 class='entry-title vcard'><a expr:href='data:post.url' expr:title='data:post.title' rel='bookmark'><b:eval expr='data:post.title ? data:post.title : data:messages.noTitle'/></a></h2>
           <b:if cond='data:widgets.Blog.first.allBylineItems.timestamp'><div class='post-snip'><span class='post-date'><time class='published' expr:datetime='data:post.date.iso8601'><data:post.date/></time></span></div></b:if>
        </div>
          <b:else/>
          <b:if cond='data:widget.sectionId not in [&quot;ft-post&quot;,&quot;hot-posts&quot;]'>
           <div class='GalaxyPSpeedSet-box'>
          <b:if cond='data:post.labels and ((data:widget.sectionId in [&quot;ft-post&quot;]) or (data:widget.sectionId == &quot;sidebar&quot; and data:i == 0))'><span class='label-news-flex'><data:post.labels.first.name/></span></b:if>
          <h2 class='entry-title vcard'><a expr:href='data:post.url' expr:title='data:post.title' rel='bookmark'><b:eval expr='data:post.title ? data:post.title : data:messages.noTitle'/></a></h2>
           <b:if cond='data:widgets.Blog.first.allBylineItems.timestamp'><div class='post-snip'><span class='post-date'><time class='published' expr:datetime='data:post.date.iso8601'><data:post.date/></time></span></div></b:if>
        </div>
         </b:if>
           <b:if cond='data:widget.sectionId == &quot;hot-posts&quot;'>
          <h2 class='entry-title vcard'><a expr:href='data:post.url' expr:title='data:post.title' rel='bookmark'><b:eval expr='data:post.title ? data:post.title : data:messages.noTitle'/></a></h2>
         </b:if>
           </b:if>
      </div>
    </b:includable>
          <b:includable id='emailPostIcon'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='facebookShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='footerBylines'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='googlePlusShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='headerByline'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='linkShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='otherSharingButton'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='platformShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postAuthor'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postCommentsLink'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postJumpLink' var='post'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postLabels'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postLocation'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postReactions'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postShareButtons'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postTimestamp'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingButton'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingButtonContent'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingButtons'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingButtonsMenu'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingPlatformIcon'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPostByline'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPostContent'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPostThumbnail'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPostTitle'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPosts'><b:comment>Replaced</b:comment></b:includable>
        </b:widget>
        <b:widget id='PopularPosts4' locked='false' title='Featured Section' type='PopularPosts' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='numItemsToShow'>6</b:widget-setting>
            <b:widget-setting name='showThumbnails'>true</b:widget-setting>
            <b:widget-setting name='showSnippets'>true</b:widget-setting>
            <b:widget-setting name='timeRange'>LAST_YEAR</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main' var='this'>
      <b:include name='widget-title'/>
      <div class='widget-content'>
        <b:if cond='data:widget.sectionId == &quot;hot-posts&quot;'>
              <b:loop index='i' values='data:posts' var='post'>
                <b:include data='post' name='content'/>
              </b:loop>
          <b:elseif cond='data:widget.sectionId == &quot;ft-post&quot;'/>
          <div class='GalaxyPSpeed-holds'>
            <b:loop index='i' values='data:posts' var='post'>
              <b:include cond='data:i in [0,1,2,3,4,5,6 7]' data='post' name='content'/>
            </b:loop>
          </div>
          <b:else/>
          <b:class name='sidebar-posts'/>
          <b:loop index='i' values='data:posts' var='post'>
            <b:include data='post' name='content'/>
          </b:loop>
        </b:if>
      </div>
    </b:includable>
          <b:includable id='blogThisShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='bylineByName' var='byline'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='bylineRegion' var='regionItems'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='commentsLink'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='commentsLinkIframe'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='content' var='post'>
      <div>
        <b:if cond='data:widget.sectionId == &quot;hot-posts&quot;'>
          <b:class name='hot-item'/>
          <b:elseif cond='data:widget.sectionId == &quot;ft-post&quot;'/>
          <b:class name='GalaxyPSpeedArea'/>
          <b:else/>
          <b:class expr:name='data:i == 0 ? &quot;popular-post post gaint-post&quot; : &quot;popular-post post&quot;'/>
        </b:if>
        <b:class expr:name='&quot;item&quot;+data:i'/>
          <b:if cond='data:widget.sectionId not in [&quot;hot-posts&quot;]'>
          <a class='post-filter-link background-layer image-nos' expr:href='data:post.url.canonical' expr:title='data:post.title ? data:post.title : data:messages.noTitle'>
          <b:if cond='data:post.featuredImage'>
          <img class='snip-thumbnail' expr:alt='data:post.title ? data:post.title : data:messages.noTitle' expr:src='data:post.featuredImage.isYouTube ? resizeImage(data:post.featuredImage.youtubeMaxResDefaultUrl.jsonEscaped, 680) : resizeImage(data:post.featuredImage, 680)'/>
          <b:else/>
          <img class='snip-thumbnail' expr:alt='data:post.title ? data:post.title : data:messages.noTitle' src='https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/w680/nth.png'/>
          </b:if><b:class expr:name='data:post.featuredImage.isYouTube ? &quot;video-nos&quot; : &quot;image-nos&quot;'/>
          </a>
          </b:if>
          <b:if cond='data:widget.sectionId == &quot;ft-post&quot;'>
           <div class='featured-meta'>
          <b:if cond='data:post.labels and ((data:widget.sectionId in [&quot;ft-post&quot;]) or (data:widget.sectionId == &quot;sidebar&quot; and data:i == 0))'><span class='label-news-flex'><data:post.labels.first.name/></span></b:if>
          <h2 class='entry-title vcard'><a expr:href='data:post.url' expr:title='data:post.title' rel='bookmark'><b:eval expr='data:post.title ? data:post.title : data:messages.noTitle'/></a></h2>
           <b:if cond='data:widgets.Blog.first.allBylineItems.timestamp'><div class='post-snip'><span class='post-date'><time class='published' expr:datetime='data:post.date.iso8601'><data:post.date/></time></span></div></b:if>
        </div>
          <b:else/>
          <b:if cond='data:widget.sectionId not in [&quot;ft-post&quot;,&quot;hot-posts&quot;]'>
           <div class='GalaxyPSpeedSet-box'>
          <b:if cond='data:post.labels and ((data:widget.sectionId in [&quot;ft-post&quot;]) or (data:widget.sectionId == &quot;sidebar&quot; and data:i == 0))'><span class='label-news-flex'><data:post.labels.first.name/></span></b:if>
          <h2 class='entry-title vcard'><a expr:href='data:post.url' expr:title='data:post.title' rel='bookmark'><b:eval expr='data:post.title ? data:post.title : data:messages.noTitle'/></a></h2>
           <b:if cond='data:widgets.Blog.first.allBylineItems.timestamp'><div class='post-snip'><span class='post-date'><time class='published' expr:datetime='data:post.date.iso8601'><data:post.date/></time></span></div></b:if>
        </div>
         </b:if>
           <b:if cond='data:widget.sectionId == &quot;hot-posts&quot;'>
          <h2 class='entry-title vcard'><a expr:href='data:post.url' expr:title='data:post.title' rel='bookmark'><b:eval expr='data:post.title ? data:post.title : data:messages.noTitle'/></a></h2>
         </b:if>
           </b:if>
      </div>
    </b:includable>
          <b:includable id='emailPostIcon'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='facebookShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='footerBylines'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='googlePlusShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='headerByline'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='linkShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='otherSharingButton'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='platformShare'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postAuthor'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postCommentsLink'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postJumpLink' var='post'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postLabels'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postLocation'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postReactions'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postShareButtons'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='postTimestamp'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingButton'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingButtonContent'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingButtons'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingButtonsMenu'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='sharingPlatformIcon'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPostByline'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPostContent'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPostThumbnail'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPostTitle'><b:comment>Replaced</b:comment></b:includable>
          <b:includable id='snippetedPosts'><b:comment>Replaced</b:comment></b:includable>
        </b:widget>
        <b:widget id='LinkList10' locked='false' title='Link List' type='LinkList' version='2' visible='false'>
          <b:widget-settings>
            <b:widget-setting name='text-10'>Documentation</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='link-1'>#</b:widget-setting>
            <b:widget-setting name='link-2'>#</b:widget-setting>
            <b:widget-setting name='link-12'>https://www.templatesyard.com/2018/08/newsplus-blog-magazine-blogger-template.html</b:widget-setting>
            <b:widget-setting name='link-0'>/</b:widget-setting>
            <b:widget-setting name='link-11'>https://youtu.be/8KMu9FWKeqo</b:widget-setting>
            <b:widget-setting name='link-10'>https://www.sorabloggingtips.com/2018/08/how-to-setup-newsplus-blogger-template.html</b:widget-setting>
            <b:widget-setting name='text-9'>Mega Menu</b:widget-setting>
            <b:widget-setting name='link-9'>Business/mega-menu</b:widget-setting>
            <b:widget-setting name='text-8'>_Error Page</b:widget-setting>
            <b:widget-setting name='link-7'>https://www.sorabloggingtips.com/2017/01/how-to-add-sitemap-widget-in-blogspot-blogs.html</b:widget-setting>
            <b:widget-setting name='link-8'>https://newsplus-templatesyard.blogspot.com/templatesyard</b:widget-setting>
            <b:widget-setting name='link-5'>#</b:widget-setting>
            <b:widget-setting name='link-6'>https://newsplus-templatesyard.blogspot.com/p/post-format-and-page-markup.html</b:widget-setting>
            <b:widget-setting name='link-3'>#</b:widget-setting>
            <b:widget-setting name='link-4'>#</b:widget-setting>
            <b:widget-setting name='text-1'>Features</b:widget-setting>
            <b:widget-setting name='text-0'>Home</b:widget-setting>
            <b:widget-setting name='text-3'>__DropDown 1</b:widget-setting>
            <b:widget-setting name='text-2'>_Multi DropDown</b:widget-setting>
            <b:widget-setting name='text-5'>__DropDown 3</b:widget-setting>
            <b:widget-setting name='text-4'>__DropDown 2</b:widget-setting>
            <b:widget-setting name='text-7'>_SiteMap</b:widget-setting>
            <b:widget-setting name='text-6'>_ShortCodes</b:widget-setting>
            <b:widget-setting name='text-11'>Video Documentation</b:widget-setting>
            <b:widget-setting name='text-12'>Download This Template</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>

<b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
   <b:include name='quickedit'/>
 </div>
</b:includable>
          <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
        </b:widget>
      </b:section>

     </div>
    <div id='ads-blog'>
      <b:section class='home-ad' id='ads-home' maxwidgets='1' name='Home ADS' showaddelement='yes'>
        <b:widget id='HTML11' locked='false' title='Ad Home' type='HTML' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='content'/>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
      </b:section>
    </div>
    </b:if>

    <b:if cond='data:blog.canonicalUrl == data:blog.canonicalHomepageUrl'>
      <div class='posts-title'>
        <h2 class='title'>
          <a href='/search'>Recent Posts</a>
        </h2>
      </div>
    </b:if>

   <b:section class='main' id='main' maxwidgets='2' name='Main Posts' showaddelement='yes'>
     <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog' version='1'>
       <b:widget-settings>
         <b:widget-setting name='showDateHeader'>true</b:widget-setting>
         <b:widget-setting name='commentLabel'>Comments</b:widget-setting>
         <b:widget-setting name='style.textcolor'>#ffffff</b:widget-setting>
         <b:widget-setting name='showShareButtons'>true</b:widget-setting>
         <b:widget-setting name='authorLabel'>By</b:widget-setting>
         <b:widget-setting name='showCommentLink'>false</b:widget-setting>
         <b:widget-setting name='style.urlcolor'>#ffffff</b:widget-setting>
         <b:widget-setting name='showAuthor'>false</b:widget-setting>
         <b:widget-setting name='style.linkcolor'>#ffffff</b:widget-setting>
         <b:widget-setting name='style.unittype'>TextAndImage</b:widget-setting>
         <b:widget-setting name='style.bgcolor'>#ffffff</b:widget-setting>
         <b:widget-setting name='reactionsLabel'/>
         <b:widget-setting name='showAuthorProfile'>false</b:widget-setting>
         <b:widget-setting name='style.layout'>1x1</b:widget-setting>
         <b:widget-setting name='showLabels'>false</b:widget-setting>
         <b:widget-setting name='showLocation'>false</b:widget-setting>
         <b:widget-setting name='postLabelsLabel'>Tags</b:widget-setting>
         <b:widget-setting name='showTimestamp'>true</b:widget-setting>
         <b:widget-setting name='postsPerAd'>1</b:widget-setting>
         <b:widget-setting name='showBacklinks'>false</b:widget-setting>
         <b:widget-setting name='style.bordercolor'>#ffffff</b:widget-setting>
         <b:widget-setting name='showInlineAds'>false</b:widget-setting>
         <b:widget-setting name='showReactions'>false</b:widget-setting>
       </b:widget-settings>
       <b:includable id='main' var='top'>
  <b:if cond='data:mobile == &quot;false&quot;'>

      <b:include data='top' name='status-message'/>

    <!-- posts -->
    <div class='blog-posts hfeed'>

      <data:defaultAdStart/>
      <b:loop values='data:posts' var='post'>
        <div class='post-outer'>
        <b:include data='post' name='post'/>
        <b:if cond='data:blog.pageType == &quot;static_page&quot;'>
          <b:include data='post' name='comment_picker'/>
        </b:if>
        <b:if cond='data:blog.pageType == &quot;item&quot;'>
          <b:include data='post' name='comment_picker'/>
        </b:if>
        </div>
        <b:if cond='data:post.includeAd'>
          <b:if cond='data:post.isFirstPost'>
            <data:defaultAdEnd/>
          <b:else/>
            <data:adEnd/>
          </b:if>
          <div class='inline-ad'>
            <data:adCode/>
          </div>
          <data:adStart/>
        </b:if>
      </b:loop>
      <data:adEnd/>
    </div>

    <!-- navigation -->
    <b:if cond='data:blog.pageType == &quot;index&quot;'>
      <b:include name='nextprev'/>
      <b:else/>
      <b:if cond='data:blog.pageType == &quot;archive&quot;'>
        <b:include name='nextprev'/>
      </b:if>
    </b:if>

    <!-- feed links -->
    <b:include name='feedLinks'/>

    <b:if cond='data:top.showStars'>
      <script src='//www.google.com/jsapi' type='text/javascript'/>
      <script type='text/javascript'>
        google.load(&quot;annotations&quot;, &quot;1&quot;, {&quot;locale&quot;: &quot;<data:top.languageCode/>&quot;});
        function initialize() {
          google.annotations.setApplicationId(<data:top.blogspotReviews/>);
          google.annotations.createAll();
          google.annotations.fetch();
        }
        google.setOnLoadCallback(initialize);
      </script>
    </b:if>

  <b:else/>
    <b:include name='mobile-main'/>
  </b:if>

  <b:if cond='data:top.showDummy'>
    <data:top.dummyBootstrap/>
  </b:if>

</b:includable>
       <b:includable id='backlinkDeleteIcon' var='backlink'>
                <span expr:class='&quot;item-control &quot; + data:backlink.adminClass'>
                  <a expr:href='data:backlink.deleteUrl' expr:title='data:top.deleteBacklinkMsg'>
                    <img src='http://www.blogger.com/img/icon_delete13.gif'/>
                  </a>
                </span>
              </b:includable>
       <b:includable id='backlinks' var='post'>
                <a name='links'/>
                <h4>
                  <data:post.backlinksLabel/>
                </h4>
                <b:if cond='data:post.numBacklinks != 0'>
                  <dl class='comments-block' id='comments-block'>
                    <b:loop values='data:post.backlinks' var='backlink'>
                      <div class='collapsed-backlink backlink-control'>
                        <dt class='comment-title'>
                          <span class='backlink-toggle-zippy'>
                            &#160;
                          </span>
                          <a expr:href='data:backlink.url' rel='nofollow'>
                            <data:backlink.title/>
                          </a>
                          <b:include data='backlink' name='backlinkDeleteIcon'/>
                        </dt>
                        <dd class='comment-body collapseable'>
                          <data:backlink.snippet/>
                        </dd>
                        <dd class='comment-footer collapseable'>
                          <span class='comment-author'>
                            <data:post.authorLabel/>
                            <data:backlink.author/>
                          </span>
                          <span class='comment-timestamp'>
                            <data:post.timestampLabel/>
                            <data:backlink.timestamp/>
                          </span>
                        </dd>
                      </div>
                    </b:loop>
                  </dl>
                </b:if>
                <p class='comment-footer'>
                  <a class='comment-link' expr:href='data:post.createLinkUrl' expr:id='data:widget.instanceId + &quot;_backlinks-create-link&quot;' target='_blank'>
                    <data:post.createLinkLabel/>
                  </a>
                </p>
              </b:includable>
       <b:includable id='comment-form' var='post'>
  <div class='comment-form'>
    <a name='comment-form'/>
    <b:if cond='data:mobile'>
      <h4 id='comment-post-message'>
        <a expr:id='data:widget.instanceId + &quot;_comment-editor-toggle-link&quot;' href='javascript:void(0)'><data:postCommentMsg/></a></h4>
      <p><data:blogCommentMessage/></p>
      <data:blogTeamBlogMessage/>
      <a expr:href='data:post.commentFormIframeSrc' id='comment-editor-src'/>
      <iframe allowtransparency='true' class='blogger-iframe-colorize blogger-comment-from-post' frameborder='0' height='410' id='comment-editor' name='comment-editor' src='' style='display: none' width='100%'/>
    <b:else/>
      <p><data:blogCommentMessage/></p>
      <data:blogTeamBlogMessage/>
      <a expr:href='data:post.commentFormIframeSrc' id='comment-editor-src'/>
      <iframe allowtransparency='true' class='blogger-iframe-colorize blogger-comment-from-post' frameborder='0' height='410' id='comment-editor' name='comment-editor' src='' width='100%'/>
    </b:if>
    <data:post.friendConnectJs/>
    <data:post.cmtfpIframe/>
    <script type='text/javascript'>
      BLOG_CMT_createIframe(&#39;<data:post.appRpcRelayPath/>&#39;);
    </script>
  </div>
</b:includable>
       <b:includable id='commentDeleteIcon' var='comment'>
  <span expr:class='&quot;item-control &quot; + data:comment.adminClass'>
    <b:if cond='data:showCmtPopup'>
      <div class='goog-toggle-button'>
        <div class='goog-inline-block comment-action-icon'/>
      </div>
    <b:else/>
      <a class='comment-delete' expr:href='data:comment.deleteUrl' expr:title='data:top.deleteCommentMsg'>
        <img src='//www.blogger.com/img/icon_delete13.gif'/>
      </a>
    </b:if>
  </span>
</b:includable>
       <b:includable id='comment_count_picker' var='post'>
  <b:if cond='data:post.commentSource == 1'>
    <span class='cmt_count_iframe_holder' expr:data-count='data:post.numComments' expr:data-onclick='data:post.addCommentOnclick' expr:data-post-url='data:post.url' expr:data-url='data:post.url.canonical.http'>
    </span>
  <b:else/>
    <a class='comment-link' expr:href='data:post.addCommentUrl' expr:onclick='data:post.addCommentOnclick'>
      <data:post.commentLabelFull/>:
    </a>
  </b:if>
</b:includable>
       <b:includable id='comment_picker' var='post'>
  <b:if cond='data:post.commentSource == 1'>
    <b:include data='post' name='iframe_comments'/>
  <b:else/>
    <b:if cond='data:post.showThreadedComments'>
      <b:include data='post' name='threaded_comments'/>
    <b:else/>
      <b:include data='post' name='comments'/>
    </b:if>
  </b:if>
</b:includable>
       <b:includable id='comments' var='post'>
  <div class='comments' id='comments'>
    <a name='comments'/>
    <b:if cond='data:post.allowComments'>
      <h4><data:post.commentLabelFull/></h4>

      <b:if cond='data:post.commentPagingRequired'>
        <span class='paging-control-container'>
          <b:if cond='data:post.hasOlderLinks'>
            <a expr:class='data:post.oldLinkClass' expr:href='data:post.oldestLinkUrl'><data:post.oldestLinkText/></a>
              &#160;
            <a expr:class='data:post.oldLinkClass' expr:href='data:post.olderLinkUrl'><data:post.olderLinkText/></a>
              &#160;
          </b:if>

          <data:post.commentRangeText/>

          <b:if cond='data:post.hasNewerLinks'>
            &#160;
            <a expr:class='data:post.newLinkClass' expr:href='data:post.newerLinkUrl'><data:post.newerLinkText/></a>
            &#160;
            <a expr:class='data:post.newLinkClass' expr:href='data:post.newestLinkUrl'><data:post.newestLinkText/></a>
          </b:if>
        </span>
      </b:if>

      <div expr:id='data:widget.instanceId + &quot;_comments-block-wrapper&quot;'>
        <dl expr:class='data:post.avatarIndentClass' id='comments-block'>
          <b:loop values='data:post.comments' var='comment'>
            <dt expr:class='&quot;comment-author &quot; + data:comment.authorClass' expr:id='data:comment.anchorName'>
              <b:if cond='data:comment.favicon'>
                <img expr:src='data:comment.favicon' height='16px' style='margin-bottom:-2px;' width='16px'/>
              </b:if>
              <a expr:name='data:comment.anchorName'/>
              <b:if cond='data:blog.enabledCommentProfileImages'>
                <data:comment.authorAvatarImage/>
              </b:if>
              <b:if cond='data:comment.authorUrl'>
                <a expr:href='data:comment.authorUrl' rel='nofollow'><data:comment.author/></a>
              <b:else/>
                <data:comment.author/>
              </b:if>
              <data:commentPostedByMsg/>
            </dt>
            <dd class='comment-body' expr:id='data:widget.instanceId + data:comment.cmtBodyIdPostfix'>
              <b:if cond='data:comment.isDeleted'>
                <span class='deleted-comment'><data:comment.body/></span>
              <b:else/>
                <p>
                  <data:comment.body/>
                </p>
              </b:if>
            </dd>
            <dd class='comment-footer'>
              <span class='comment-timestamp'>
                <a expr:href='data:comment.url' title='comment permalink'>
                  <abbr expr:title='data:post.timestampISO8601'><data:comment.timestamp/></abbr>
                </a>
                <b:include data='comment' name='commentDeleteIcon'/>
              </span>
            </dd>
          </b:loop>
        </dl>
      </div>

      <b:if cond='data:post.commentPagingRequired'>
        <span class='paging-control-container'>
          <a expr:class='data:post.oldLinkClass' expr:href='data:post.oldestLinkUrl'>
            <data:post.oldestLinkText/>
          </a>
          <a expr:class='data:post.oldLinkClass' expr:href='data:post.olderLinkUrl'>
            <data:post.olderLinkText/>
          </a>
          &#160;
          <data:post.commentRangeText/>
          &#160;
          <a expr:class='data:post.newLinkClass' expr:href='data:post.newerLinkUrl'>
            <data:post.newerLinkText/>
          </a>
          <a expr:class='data:post.newLinkClass' expr:href='data:post.newestLinkUrl'>
            <data:post.newestLinkText/>
          </a>
        </span>
      </b:if>

      <p class='comment-footer'>
        <b:if cond='data:post.embedCommentForm'>
          <b:if cond='data:post.allowNewComments'>
            <b:include data='post' name='comment-form'/>
          <b:else/>
            <data:post.noNewCommentsText/>
          </b:if>
        <b:else/>
          <b:if cond='data:post.allowComments'>
            <a expr:href='data:post.addCommentUrl' expr:onclick='data:post.addCommentOnclick'><data:postCommentMsg/></a>
          </b:if>
        </b:if>

      </p>
    </b:if>
    <b:if cond='data:showCmtPopup'>
      <div id='comment-popup'>
        <iframe allowtransparency='true' frameborder='0' id='comment-actions' name='comment-actions' scrolling='no'>
        </iframe>
      </div>
    </b:if>

    <div id='backlinks-container'>
    <div expr:id='data:widget.instanceId + &quot;_backlinks-container&quot;'>
       <b:if cond='data:post.showBacklinks'>
         <b:include data='post' name='backlinks'/>
       </b:if>
    </div>
    </div>
  </div>
</b:includable>
       <b:includable id='feedLinks'>
                <b:if cond='data:blog.pageType != &quot;item&quot;'>
                  <!-- Blog feed links -->
                  <b:if cond='data:feedLinks'>
                    <div class='blog-feeds'>
                      <b:include data='feedLinks' name='feedLinksBody'/>
                    </div>
                  </b:if>
                  <b:else/>
                  <!--Post feed links -->
                  <div class='post-feeds'>
                    <b:loop values='data:posts' var='post'>
                      <b:if cond='data:post.allowComments'>
                        <b:if cond='data:post.feedLinks'>
                          <b:include data='post.feedLinks' name='feedLinksBody'/>
                        </b:if>
                      </b:if>
                    </b:loop>
                  </div>
                </b:if>
              </b:includable>
       <b:includable id='feedLinksBody' var='links'>
                <div class='feed-links'>
                  <data:feedLinksMsg/>
                  <b:loop values='data:links' var='f'>
                    <a class='feed-link' expr:href='data:f.url' expr:type='data:f.mimeType' target='_blank'>
                      <data:f.name/>
                      (
                      <data:f.feedType/>
                      )
                    </a>
                  </b:loop>
                </div>
              </b:includable>
       <b:includable id='iframe_comments' var='post'>

  <b:if cond='data:post.allowIframeComments'>
    <script expr:src='data:post.iframeCommentSrc' type='text/javascript'/>
    <div class='cmt_iframe_holder' expr:data-href='data:post.url.canonical' expr:data-viewtype='data:post.viewType'/>

    <b:if cond='data:post.embedCommentForm == &quot;false&quot;'>
      <a expr:href='data:post.addCommentUrl' expr:onclick='data:post.addCommentOnclick'><data:postCommentMsg/></a>
    </b:if>
  </b:if>
</b:includable>
       <b:includable id='mobile-index-post' var='post'>
                <div class='mobile-date-outer date-outer'>
                  <b:if cond='data:post.dateHeader'>
                    <div class='date-header'>
                      <span>
                        <data:post.dateHeader/>
                      </span>
                    </div>
                  </b:if>
                  <div class='mobile-post-outer'>
                    <a expr:href='data:post.url'>
                      <h3 class='mobile-index-title entry-title' itemprop='name'>
                        <data:post.title/>
                      </h3>
                      <div class='mobile-index-arrow'>
                        &amp;rsaquo;
                      </div>
                      <div class='mobile-index-contents'>
                        <b:if cond='data:post.thumbnailUrl'>
                          <div class='mobile-index-thumbnail'>
                            <div class='Image'>
                              <img expr:src='data:post.thumbnailUrl'/>
                            </div>
                          </div>
                        </b:if>
                        <div class='post-body'>
                          <b:if cond='data:post.snippet'>
                            <data:post.snippet/>
                          </b:if>
                        </div>
                      </div>
                      <div style='clear: both;'/>
                    </a>
                    <div class='mobile-index-comment'>
                      <b:if cond='data:blog.pageType != &quot;static_page&quot;'>
                        <b:if cond='data:post.allowComments'>
                          <b:if cond='data:post.numComments != 0'>
                            <b:include data='post' name='comment_count_picker'/>
                          </b:if>
                        </b:if>
                      </b:if>
                    </div>
                  </div>
                </div>
              </b:includable>
       <b:includable id='mobile-main' var='top'>
                <!-- posts -->
                <div class='blog-posts hfeed'>
                  <b:include data='top' name='status-message'/>
                  <b:if cond='data:blog.pageType == &quot;index&quot;'>
                    <b:loop values='data:posts' var='post'>
                      <b:include data='post' name='mobile-index-post'/>
                    </b:loop>
                    <b:else/>
                    <b:loop values='data:posts' var='post'>
                      <b:include data='post' name='mobile-post'/>
                    </b:loop>
                  </b:if>
                </div>
                <b:include name='mobile-nextprev'/>
              </b:includable>
       <b:includable id='mobile-nextprev'>
                <div class='blog-pager' id='blog-pager'>
                  <b:if cond='data:newerPageUrl'>
                    <div class='mobile-link-button' id='blog-pager-newer-link'>
                      <a class='blog-pager-newer-link' expr:href='data:newerPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-newer-link&quot;' expr:title='data:newerPageTitle'>
                        &amp;lsaquo;
                      </a>
                    </div>
                  </b:if>
                  <b:if cond='data:olderPageUrl'>
                    <div class='mobile-link-button' id='blog-pager-older-link'>
                      <a class='blog-pager-older-link' expr:href='data:olderPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-older-link&quot;' expr:title='data:olderPageTitle'>
                        &amp;rsaquo;
                      </a>
                    </div>
                  </b:if>
                  <div class='mobile-link-button' id='blog-pager-home-link'>
                    <a class='home-link' expr:href='data:blog.homepageUrl'>
                      <data:homeMsg/>
                    </a>
                  </div>
                  <div class='mobile-desktop-link'>
                    <a class='home-link' expr:href='data:desktopLinkUrl'>
                      <data:desktopLinkMsg/>
                    </a>
                  </div>
                </div>
                <div class='clear'/>
              </b:includable>
       <b:includable id='mobile-post' var='post'>
                <div class='date-outer'>
                  <b:if cond='data:post.dateHeader'>
                    <h2 class='date-header'>
                      <span>
                        <data:post.dateHeader/>
                      </span>
                    </h2>
                  </b:if>
                  <div class='date-posts'>
                    <div class='post-outer'>
                      <div class='post hentry uncustomized-post-template' itemscope='' itemtype='http://schema.org/BlogPosting'>
                        <b:if cond='data:post.thumbnailUrl'>
                          <meta expr:content='data:post.thumbnailUrl' itemprop='image'/>
                        </b:if>
                        <meta expr:content='data:blog.blogId' itemprop='blogId'/>
                        <meta expr:content='data:post.id' itemprop='postId'/>
                        <a expr:name='data:post.id'/>
                        <b:if cond='data:post.title'>
                          <h3 class='post-title entry-title' itemprop='headline'>
                            <b:if cond='data:post.link'>
                              <a expr:href='data:post.link'>
                                <data:post.title/>
                              </a>
                              <b:else/>
                              <b:if cond='data:post.url'>
                                <b:if cond='data:blog.url != data:post.url'>
                                  <a expr:href='data:post.url'>
                                    <data:post.title/>
                                  </a>
                                  <b:else/>
                                  <data:post.title/>
                                </b:if>
                                <b:else/>
                                <data:post.title/>
                              </b:if>
                            </b:if>
                          </h3>
                        </b:if>
                        <div class='post-header'>
                          <div class='post-header-line-1'/>
                        </div>
                        <div class='post-body entry-content' expr:id='&quot;post-body-&quot; + data:post.id' itemprop='articleBody'>
                          <data:post.body/>
                          <div style='clear: both;'/>
                          <!-- clear for photos floats -->
                        </div>
                        <div class='post-footer'>
                          <div class='post-footer-line post-footer-line-1'>
                            <span class='post-author vcard'>
                              <b:if cond='data:top.showAuthor'>
                                <b:if cond='data:post.authorProfileUrl'>
                                  <span class='fn' itemprop='author' itemscope='' itemtype='http://schema.org/Person'>
                                    <meta expr:content='data:post.authorProfileUrl' itemprop='url'/>
                                    <a expr:href='data:post.authorProfileUrl' rel='author' title='author profile'>
                                      <span itemprop='name'>
                                        <data:post.author/>
                                      </span>
                                    </a>
                                  </span>
                                  <b:else/>
                                  <span class='fn' itemprop='author' itemscope='' itemtype='http://schema.org/Person'>
                                    <span itemprop='name'>
                                      <data:post.author/>
                                    </span>
                                  </span>
                                </b:if>
                              </b:if>
                            </span>
                            <span class='post-timestamp'>
                              <b:if cond='data:top.showTimestamp'>
                                <data:top.timestampLabel/>
                                <b:if cond='data:post.url'>
                                  <meta expr:content='data:post.canonicalUrl' itemprop='url'/>
                                  <a class='timestamp-link' expr:href='data:post.url' expr:title='data:post.timestamp' rel='bookmark'>
                                    <abbr class='published' expr:title='data:post.timestamp' itemprop='datePublished dateModified'>
                                      <data:post.timestamp/>
                                    </abbr>
                                  </a>
                                </b:if>
                              </b:if>
                            </span>
                            <span class='post-comment-link'>
                              <b:if cond='data:blog.pageType != &quot;item&quot;'>
                                <b:if cond='data:blog.pageType != &quot;static_page&quot;'>
                                  <b:if cond='data:post.allowComments'>
                                    <b:include data='post' name='comment_count_picker'/>
                                  </b:if>
                                </b:if>
                              </b:if>
                            </span>
                          </div>
                          <div class='post-footer-line post-footer-line-2'>
                            <b:if cond='data:top.showMobileShare'>
                              <div class='mobile-link-button goog-inline-block' id='mobile-share-button'>
                                <a href='javascript:void(0);'>
                                  <data:shareMsg/>
                                </a>
                              </div>
                            </b:if>
                            <b:if cond='data:top.showDummy'>
                              <div class='goog-inline-block dummy-container'>
                                <data:post.dummyTag/>
                              </div>
                            </b:if>
                          </div>
                        </div>
                      </div>
                      <b:if cond='data:blog.pageType == &quot;static_page&quot;'>
                        <b:include data='post' name='comment_picker'/>
                      </b:if>
                      <b:if cond='data:blog.pageType == &quot;item&quot;'>
                        <b:include data='post' name='comment_picker'/>
                      </b:if>
                    </div>
                  </div>
                </div>
              </b:includable>
       <b:includable id='nextprev'>
  <div class='blog-pager' id='blog-pager'>
    <b:if cond='data:newerPageUrl'>
      <span id='blog-pager-newer-link'>
      <a class='blog-pager-newer-link' expr:href='data:newerPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-newer-link&quot;' expr:title='data:newerPageTitle'><data:newerPageTitle/></a>
      </span>
    </b:if>

    <b:if cond='data:olderPageUrl'>
      <span id='blog-pager-older-link'>
      <a class='blog-pager-older-link' expr:href='data:olderPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-older-link&quot;' expr:title='data:olderPageTitle'><data:olderPageTitle/></a>
      </span>
    </b:if>

    <a class='home-link' expr:href='data:blog.homepageUrl'><data:homeMsg/></a>

    <b:if cond='data:mobileLinkUrl'>
      <div class='blog-mobile-link'>
        <a expr:href='data:mobileLinkUrl'><data:mobileLinkMsg/></a>
      </div>
    </b:if>

  </div>
  <div class='clear'/>
</b:includable>
       <b:includable id='post' var='post'>
         <div class='post'>
           <b:if cond='data:blog.pageType == &quot;index&quot;'>
             <b:if cond='data:post.thumbnailUrl'>
               <div class='block-image'><div class='thumb'>
                 &lt;a href=&#39;<data:post.url/>&#39; style=&#39;background:url(<data:post.thumbnailUrl/>) no-repeat center center;background-size:cover&#39;&gt;&lt;span class=&#39;thumb-overlay&#39;/&gt;&lt;/a&gt;
                 </div>
                 <div class='postags'>
                   <b:if cond='data:post.labels'>
                     <b:loop values='data:post.labels' var='label'>
                       <a expr:class='data:label.name' expr:href='data:label.url' rel='tag'><data:label.name/></a>
                       <b:if cond='data:label.isLast != &quot;true&quot;'/>
                     </b:loop>
                   </b:if>
                 </div></div>
               <b:else/>
               <b:if cond='data:post.firstImageUrl'>
                 <div class='block-image'><div class='thumb'>
                   &lt;a href=&#39;<data:post.url/>&#39; style=&#39;background:url(<data:post.firstImageUrl/>) no-repeat center center;background-size:cover&#39;&gt;&lt;span class=&#39;thumb-overlay&#39;/&gt;&lt;/a&gt;
                   </div>
                   <div class='postags'>
                     <b:if cond='data:post.labels'>
                       <b:loop values='data:post.labels' var='label'>
                         <a expr:class='data:label.name' expr:href='data:label.url' rel='tag'><data:label.name/></a>
                         <b:if cond='data:label.isLast != &quot;true&quot;'/>
                       </b:loop>
                     </b:if>
                   </div></div>
                 <b:else/>
                 <div class='block-image'><div class='thumb'>
                   &lt;a href=&#39;<data:post.url/>&#39; style=&#39;background:url(http://3.bp.blogspot.com/-Yw8BIuvwoSQ/VsjkCIMoltI/AAAAAAAAC4c/s55PW6xEKn0/s1600-r/nth.png) no-repeat center center;background-size:cover&#39;&gt;&lt;span class=&#39;thumb-overlay&#39;/&gt;&lt;/a&gt;
                   </div>
                   <div class='postags'>
                     <b:if cond='data:post.labels'>
                       <b:loop values='data:post.labels' var='label'>
                         <a expr:class='data:label.name' expr:href='data:label.url' rel='tag'><data:label.name/></a>
                         <b:if cond='data:label.isLast != &quot;true&quot;'/>
                       </b:loop>
                     </b:if>
                   </div></div>
               </b:if></b:if>
           </b:if>
           <b:if cond='data:blog.pageType == &quot;archive&quot;'>
             <b:if cond='data:post.thumbnailUrl'>
               <div class='block-image'><div class='thumb'>
                 &lt;a href=&#39;<data:post.url/>&#39; style=&#39;background:url(<data:post.thumbnailUrl/>) no-repeat center center;background-size:cover&#39;&gt;&lt;span class=&#39;thumb-overlay&#39;/&gt;&lt;/a&gt;
                 </div>
                 <div class='postags'>
                   <b:if cond='data:post.labels'>
                     <b:loop values='data:post.labels' var='label'>
                       <a expr:class='data:label.name' expr:href='data:label.url' rel='tag'><data:label.name/></a>
                       <b:if cond='data:label.isLast != &quot;true&quot;'/>
                     </b:loop>
                   </b:if>
                 </div></div>
               <b:else/>
               <b:if cond='data:post.firstImageUrl'>
                 <div class='block-image'><div class='thumb'>
                   &lt;a href=&#39;<data:post.url/>&#39; style=&#39;background:url(<data:post.firstImageUrl/>) no-repeat center center;background-size:cover&#39;&gt;&lt;span class=&#39;thumb-overlay&#39;/&gt;&lt;/a&gt;
                   </div>
                   <div class='postags'>
                     <b:if cond='data:post.labels'>
                       <b:loop values='data:post.labels' var='label'>
                         <a expr:class='data:label.name' expr:href='data:label.url' rel='tag'><data:label.name/></a>
                         <b:if cond='data:label.isLast != &quot;true&quot;'/>
                       </b:loop>
                     </b:if>
                   </div></div>
                 <b:else/>
                 <div class='block-image'><div class='thumb'>
                   &lt;a href=&#39;<data:post.url/>&#39; style=&#39;background:url(http://3.bp.blogspot.com/-Yw8BIuvwoSQ/VsjkCIMoltI/AAAAAAAAC4c/s55PW6xEKn0/s1600-r/nth.png) no-repeat center center;background-size:cover&#39;&gt;&lt;span class=&#39;thumb-overlay&#39;/&gt;&lt;/a&gt;
                   </div>
                   <div class='postags'>
                     <b:if cond='data:post.labels'>
                       <b:loop values='data:post.labels' var='label'>
                         <a expr:class='data:label.name' expr:href='data:label.url' rel='tag'><data:label.name/></a>
                         <b:if cond='data:label.isLast != &quot;true&quot;'/>
                       </b:loop>
                     </b:if>
                   </div></div>
               </b:if></b:if>
           </b:if>
           <b:if cond='data:blog.pageType == &quot;item&quot;'>
             &lt;div itemprop=&#39;blogPost&#39; itemscope=&#39;itemscope&#39; itemtype=&#39;http://schema.org/BlogPosting&#39;&gt;
               <meta expr:content='data:post.firstImageUrl' itemprop='image'/>
           </b:if>
           <div class='post-header'>
             <b:if cond='data:blog.pageType == &quot;item&quot;'>
               <div class='breadcrumbs' xmlns:v='http://rdf.data-vocabulary.org/#'>
                 <span typeof='v:Breadcrumb'><a class='bhome' expr:href='data:blog.homepageUrl' property='v:title' rel='v:url'>Home</a></span> <brc>&gt;</brc>
                 <b:loop values='data:posts' var='post'>
                   <b:if cond='data:post.labels'>
                     <b:loop values='data:post.labels' var='label'>
                       <span typeof='v:Breadcrumb'>
                         <a expr:href='data:label.url' property='v:title' rel='v:url'><data:label.name/></a></span>
                       <b:if cond='data:label.isLast != &quot;true&quot;'><brc>&gt;</brc></b:if>
                     </b:loop>
                     <b:else/>
                     Unlabelled
                   </b:if>
                   <brc>&gt;</brc> <span><data:post.title/></span>
                 </b:loop>
               </div>
               <b:if cond='data:post.title'>
                 <div class='post-head'><h1 class='post-title entry-title' itemprop='name headline'>
                   <b:if cond='data:post.link'>
                     <a expr:href='data:post.link'><data:post.title/></a>
                     <b:else/>
                     <b:if cond='data:post.url'>
                       <b:if cond='data:blog.url != data:post.url'>
                         <a expr:href='data:post.url'><data:post.title/></a>
                         <b:else/>
                         <data:post.title/>
                       </b:if>
                       <b:else/>
                       <data:post.title/>
                     </b:if>
                   </b:if>
                   </h1></div>
               </b:if>
               <div class='post-meta'>
                 <span class='post-author vcard'>
                   <b:if cond='data:top.showAuthor'>
                     <b:if cond='data:post.authorProfileUrl'>
                       <span class='fn' itemprop='author' itemscope='itemscope' itemtype='http://schema.org/Person'>
                         <meta expr:content='data:post.authorProfileUrl' itemprop='url'/>
                         <a class='g-profile' expr:href='data:post.authorProfileUrl' expr:title='data:post.author' rel='author'>
                           <span itemprop='name'><data:post.author/></span>
                         </a>
                       </span>
                       <b:else/>
                       <span class='fn' itemprop='author' itemscope='itemscope' itemtype='http://schema.org/Person'>
                         <a class='g-profile' expr:href='data:post.authorProfileUrl' expr:title='data:post.author' rel='author'>
                           <span itemprop='name'><data:post.author/></span></a>
                       </span>
                     </b:if>
                   </b:if>
                 </span>
                 <span class='post-timestamp'>
                   <b:if cond='data:top.showTimestamp'>
                     <b:if cond='data:post.url'>
                       <meta expr:content='data:post.canonicalUrl' itemprop='url mainEntityOfPage'/>
                       <a class='timestamp-link' expr:href='data:post.url' rel='bookmark' title='permanent link'><abbr class='published' expr:title='data:post.timestampISO8601' itemprop='datePublished dateModified'><data:post.timestamp/></abbr></a>
                     </b:if>
                   </b:if>
                 </span>
                 <span class='label-head'>
                   <b:if cond='data:post.labels'>
                     <b:loop values='data:post.labels' var='label'>
                       <a expr:href='data:label.url' rel='tag'><data:label.name/></a><b:if cond='data:label.isLast != &quot;true&quot;'>,</b:if>
                     </b:loop>
                   </b:if>
                 </span>
               </div>
             </b:if>
             <b:if cond='data:blog.pageType == &quot;static_page&quot;'>
               <b:if cond='data:post.title'>
                 <div class='post-head'><h1 class='post-title entry-title' itemprop='name headline'>
                   <b:if cond='data:post.link'>
                     <a expr:href='data:post.link'><data:post.title/></a>
                     <b:else/>
                     <b:if cond='data:post.url'>
                       <b:if cond='data:blog.url != data:post.url'>
                         <a expr:href='data:post.url'><data:post.title/></a>
                         <b:else/>
                         <data:post.title/>
                       </b:if>
                       <b:else/>
                       <data:post.title/>
                     </b:if>
                   </b:if>
                   </h1></div>
               </b:if>
             </b:if>
           </div>
           <article>
             <b:if cond='data:blog.pageType != &quot;item&quot;'>
               <b:if cond='data:blog.pageType != &quot;static_page&quot;'>
                 <b:if cond='data:post.title'>
                   <font class='retitle'>
                     <h2 class='post-title entry-title'>
                       <b:if cond='data:post.link'>
                         <a expr:href='data:post.link'>
                           <data:post.title/>
                         </a>
                         <b:else/>
                         <b:if cond='data:post.url'>
                           <a expr:href='data:post.url'>
                             <data:post.title/>
                           </a>
                           <b:else/>
                           <data:post.title/>
                         </b:if>
                       </b:if>
                     </h2>
                   </font>
                 </b:if>
                 <div class='date-header'>
                   <div id='meta-post'>
                     <a class='timestamp-link' expr:href='data:post.url' rel='bookmark' title='permanent link'><abbr class='published' expr:title='data:post.timestampISO8601' itemprop='datePublished dateModified'><data:post.timestamp/></abbr></a></div><div class='resumo'><span><data:post.snippet/></span><a class='read-more' expr:href='data:post.url'>Read More</a></div>
                   <div style='clear: both;'/>
                 </div>
                 <b:else/>
                 <div class='post-body entry-content' expr:id='&quot;post-body-&quot; + data:post.id' itemprop='articleBody'>
                   <meta expr:content='data:post.snippet' name='twitter:description'/>
                   <data:post.body/>
                 </div>
               </b:if>
               <b:else/>
               <div class='post-body entry-content' expr:id='&quot;post-body-&quot; + data:post.id' itemprop='articleBody'>
                 <meta expr:content='data:post.snippet' name='twitter:description'/>
                 <data:post.body/>
               </div>
             </b:if>
           </article>
           <div style='clear:both'/>  
           <div class='post-footer'>
             <b:if cond='data:blog.pageType == &quot;item&quot;'>
               <div class='share-box'>
                 
                <div class='share-art'>

                  <div class='sa-title'>
                    <strong>SHARE THIS</strong>
                  </div>

                  <a class='facebook' expr:href='&quot;http://www.facebook.com/sharer.php?u=&quot; + data:post.url + &quot;&amp;title=&quot;+ data:post.title' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=600, height=400, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow' target='_blank'><i class='fa fa-facebook'/><span> Share it</span></a>

                  <a class='twitter' expr:href='&quot;http://twitter.com/share?url=&quot; + data:post.url + &quot;&amp;title=&quot; + data:post.title' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=600, height=400, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow' target='_blank'><i class='fa fa-twitter'/><span> Tweet</span></a>

                  <a class='googleplus' expr:href='&quot;https://plus.google.com/share?url=&quot; + data:post.url + &quot;&amp;title=&quot; + data:post.title' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=600, height=400, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow' target='_blank'><i class='fa fa-google-plus'/><span> Share it</span></a>

                  <a class='linkedin' expr:href='&quot;http://www.linkedin.com/shareArticle?url=&quot; + data:post.url + &quot;&amp;title=&quot;+ data:post.title' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=600, height=400, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow' target='_blank'><i class='fa fa-linkedin'/><span> Share it</span></a>

                  <a class='pinterest' expr:href='&quot;http://pinterest.com/pin/create/button/?url=&quot; + data:post.url + &quot;&amp;media=&quot; + data:post.firstImageUrl + &quot;&amp;description=&quot; + data:post.snippet' onclick='window.open(this.href, &apos;windowName&apos;, &apos;width=600, height=400, left=24, top=24, scrollbars, resizable&apos;); return false;' rel='nofollow' target='_blank'><i class='fa fa-pinterest-p'/><span> Pin it</span></a>  

                </div>
               </div>

                <div style='clear:both'/>  

               <div id='related-wrap'>
                 <div class='related-title'>
                   <h2>Related Posts</h2>
                 </div>
                 <div id='related-ready'>
                   <b:if cond='data:post.labels'>
                     <b:loop values='data:post.labels' var='label'>
                       <b:if cond='data:label.isLast == &quot;true&quot;'>
                         <data:label.name/>
                       </b:if>
                     </b:loop>
                   </b:if>
                 </div>   
               </div>        

               <div style='clear:both'/>  

               <ul class='ib-nav'>
                 <li class='next'> 
                   <b:if cond='data:newerPageUrl'> 
                     <a class='newer-link' expr:href='data:newerPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-newer-link&quot;' rel='next'/> 
                     <b:else/> 
                     <a rel='next'><strong>Next</strong><span>You are viewing Most Recent Post</span></a> 
                   </b:if> 
                 </li>
                 <li class='previous'> 
                   <b:if cond='data:olderPageUrl'> 
                     <a class='older-link' expr:href='data:olderPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-older-link&quot;' rel='previous'/> 
                     <b:else/> 
                     <a rel='previous'><strong>Previous</strong><span>You are viewing Last Post</span></a> 
                   </b:if> 
                 </li>
               </ul>

               <div style='clear:both'/>

               <div class='comments-title'>
                 <h2>Post a Comment</h2>
               </div>
             </b:if>
           </div>    

           <b:if cond='data:blog.pageType == &quot;item&quot;'>
             <div itemprop='publisher' itemscope='itemscope' itemtype='https://schema.org/Organization' style='display:none;'>
               <div itemprop='logo' itemscope='itemscope' itemtype='https://schema.org/ImageObject'>
                 <meta expr:content='data:post.firstImageUrl' itemprop='url'/>
               </div>
               <meta expr:content='data:blog.title' itemprop='name'/>
             </div>
             &lt;/div&gt;
           </b:if>

         </div>
       </b:includable>
       <b:includable id='postQuickEdit' var='post'>
                      <b:if cond='data:post.editUrl'>
                        <span expr:class='&quot;item-control &quot; + data:post.adminClass'>
                          <a expr:href='data:post.editUrl' expr:title='data:top.editPostMsg'>
                            <!-- <img alt='' class='icon-action' height='18' src='http://img2.blogblog.com/img/icon18_edit_allbkg.gif' width='18'/> -->
                            <b style='color: #dd4b39;margin-left: 5px;'>
                              <i class='fa fa-pencil'/>
                              Edit
                            </b>
                          </a>
                        </span>
                      </b:if>
                    </b:includable>
       <b:includable id='shareButtons' var='post'>
                <b:if cond='data:top.showEmailButton'>
                  <a class='goog-inline-block share-button sb-email' expr:href='data:post.sharePostUrl + &quot;&amp;target=email&quot;' expr:title='data:top.emailThisMsg' target='_blank'>
                    <span class='share-button-link-text'>
                      <data:top.emailThisMsg/>
                    </span>
                  </a>
                </b:if>
                <b:if cond='data:top.showBlogThisButton'>
                  <a class='goog-inline-block share-button sb-blog' expr:href='data:post.sharePostUrl + &quot;&amp;target=blog&quot;' expr:onclick='&quot;window.open(this.href, \&quot;_blank\&quot;, \&quot;height=270,width=475\&quot;); return false;&quot;' expr:title='data:top.blogThisMsg' target='_blank'>
                    <span class='share-button-link-text'>
                      <data:top.blogThisMsg/>
                    </span>
                  </a>
                </b:if>
                <b:if cond='data:top.showTwitterButton'>
                  <a class='goog-inline-block share-button sb-twitter' expr:href='data:post.sharePostUrl + &quot;&amp;target=twitter&quot;' expr:title='data:top.shareToTwitterMsg' target='_blank'>
                    <span class='share-button-link-text'>
                      <data:top.shareToTwitterMsg/>
                    </span>
                  </a>
                </b:if>
                <b:if cond='data:top.showFacebookButton'>
                  <a class='goog-inline-block share-button sb-facebook' expr:href='data:post.sharePostUrl + &quot;&amp;target=facebook&quot;' expr:onclick='&quot;window.open(this.href, \&quot;_blank\&quot;, \&quot;height=430,width=640\&quot;); return false;&quot;' expr:title='data:top.shareToFacebookMsg' target='_blank'>
                    <span class='share-button-link-text'>
                      <data:top.shareToFacebookMsg/>
                    </span>
                  </a>
                </b:if>
                <b:if cond='data:top.showOrkutButton'>
                  <a class='goog-inline-block share-button sb-orkut' expr:href='data:post.sharePostUrl + &quot;&amp;target=orkut&quot;' expr:title='data:top.shareToOrkutMsg' target='_blank'>
                    <span class='share-button-link-text'>
                      <data:top.shareToOrkutMsg/>
                    </span>
                  </a>
                </b:if>
                <b:if cond='data:top.showDummy'>
                  <div class='goog-inline-block dummy-container'>
                    <data:post.dummyTag/>
                  </div>
                </b:if>
              </b:includable>
       <b:includable id='status-message'>
        <b:if cond='data:navMessage'>
            <div class='status-msg-wrap'>
             <div class='status-msg-body'>
              <data:navMessage/>
              </div>
               <div class='status-msg-border'>
                <div class='status-msg-bg'>
                <div class='status-msg-hidden'><data:navMessage/></div>
               </div>
             </div>
             </div>
           <div style='clear: both;'/>
          </b:if>
        </b:includable>
       <b:includable id='threaded-comment-form' var='post'>
  <div class='comment-form'>
    <a name='comment-form'/>
    <b:if cond='data:mobile'>
      <p><data:blogCommentMessage/></p>
      <data:blogTeamBlogMessage/>
      <a expr:href='data:post.commentFormIframeSrc' id='comment-editor-src'/>
      <iframe allowtransparency='true' class='blogger-iframe-colorize blogger-comment-from-post' frameborder='0' height='410' id='comment-editor' name='comment-editor' src='' style='display: none' width='100%'/>
    <b:else/>
      <p><data:blogCommentMessage/></p>
      <data:blogTeamBlogMessage/>
      <a expr:href='data:post.commentFormIframeSrc' id='comment-editor-src'/>
      <iframe allowtransparency='true' class='blogger-iframe-colorize blogger-comment-from-post' frameborder='0' height='410' id='comment-editor' name='comment-editor' src='' width='100%'/>
    </b:if>
    <data:post.friendConnectJs/>
    <data:post.cmtfpIframe/>
    <script type='text/javascript'>
      BLOG_CMT_createIframe(&#39;<data:post.appRpcRelayPath/>&#39;);
    </script>
  </div>
</b:includable>
       <b:includable id='threaded_comment_js' var='post'>
  <script async='async' expr:src='data:post.commentSrc' type='text/javascript'/>

  <script type='text/javascript'>
    (function() {
      var items = <data:post.commentJso/>;
      var msgs = <data:post.commentMsgs/>;
      var config = <data:post.commentConfig/>;

// <![CDATA[
      var cursor = null;
      if (items && items.length > 0) {
        cursor = parseInt(items[items.length - 1].timestamp) + 1;
      }

      var bodyFromEntry = function(entry) {
        if (entry.gd$extendedProperty) {
          for (var k in entry.gd$extendedProperty) {
            if (entry.gd$extendedProperty[k].name == 'blogger.contentRemoved') {
              return '<span class="deleted-comment">' + entry.content.$t + '</span>';
            }
          }
        }
        return entry.content.$t;
      }

      var parse = function(data) {
        cursor = null;
        var comments = [];
        if (data && data.feed && data.feed.entry) {
          for (var i = 0, entry; entry = data.feed.entry[i]; i++) {
            var comment = {};
            // comment ID, parsed out of the original id format
            var id = /blog-(\d+).post-(\d+)/.exec(entry.id.$t);
            comment.id = id ? id[2] : null;
            comment.body = bodyFromEntry(entry);
            comment.timestamp = Date.parse(entry.published.$t) + '';
            if (entry.author && entry.author.constructor === Array) {
              var auth = entry.author[0];
              if (auth) {
                comment.author = {
                  name: (auth.name ? auth.name.$t : undefined),
                  profileUrl: (auth.uri ? auth.uri.$t : undefined),
                  avatarUrl: (auth.gd$image ? auth.gd$image.src : undefined)
                };
              }
            }
            if (entry.link) {
              if (entry.link[2]) {
                comment.link = comment.permalink = entry.link[2].href;
              }
              if (entry.link[3]) {
                var pid = /.*comments\/default\/(\d+)\?.*/.exec(entry.link[3].href);
                if (pid && pid[1]) {
                  comment.parentId = pid[1];
                }
              }
            }
            comment.deleteclass = 'item-control blog-admin';
            if (entry.gd$extendedProperty) {
              for (var k in entry.gd$extendedProperty) {
                if (entry.gd$extendedProperty[k].name == 'blogger.itemClass') {
                  comment.deleteclass += ' ' + entry.gd$extendedProperty[k].value;
                } else if (entry.gd$extendedProperty[k].name == 'blogger.displayTime') {
                  comment.displayTime = entry.gd$extendedProperty[k].value;
                }
              }
            }
            comments.push(comment);
          }
        }
        return comments;
      };

      var paginator = function(callback) {
        if (hasMore()) {
          var url = config.feed + '?alt=json&v=2&orderby=published&reverse=false&max-results=50';
          if (cursor) {
            url += '&published-min=' + new Date(cursor).toISOString();
          }
          window.bloggercomments = function(data) {
            var parsed = parse(data);
            cursor = parsed.length < 50 ? null
                : parseInt(parsed[parsed.length - 1].timestamp) + 1
            callback(parsed);
            window.bloggercomments = null;
          }
          url += '&callback=bloggercomments';
          var script = document.createElement('script');
          script.type = 'text/javascript';
          script.src = url;
          document.getElementsByTagName('head')[0].appendChild(script);
        }
      };
      var hasMore = function() {
        return !!cursor;
      };
      var getMeta = function(key, comment) {
        if ('iswriter' == key) {
          var matches = !!comment.author
              && comment.author.name == config.authorName
              && comment.author.profileUrl == config.authorUrl;
          return matches ? 'true' : '';
        } else if ('deletelink' == key) {
          return config.baseUri + '/delete-comment.g?blogID='
               + config.blogId + '&postID=' + comment.id;
        } else if ('deleteclass' == key) {
          return comment.deleteclass;
        }
        return '';
      };

      var replybox = null;
      var replyUrlParts = null;
      var replyParent = undefined;

      var onReply = function(commentId, domId) {
        if (replybox == null) {
          // lazily cache replybox, and adjust to suit this style:
          replybox = document.getElementById('comment-editor');
          if (replybox != null) {
            replybox.height = '250px';
            replybox.style.display = 'block';
            replyUrlParts = replybox.src.split('#');
          }
        }
        if (replybox && (commentId !== replyParent)) {
          document.getElementById(domId).insertBefore(replybox, null);
          replybox.src = replyUrlParts[0]
              + (commentId ? '&parentID=' + commentId : '')
              + '#' + replyUrlParts[1];
          replyParent = commentId;
        }
      };

      var hash = (window.location.hash || '#').substring(1);
      var startThread, targetComment;
      if (/^comment-form_/.test(hash)) {
        startThread = hash.substring('comment-form_'.length);
      } else if (/^c[0-9]+$/.test(hash)) {
        targetComment = hash.substring(1);
      }

      // Configure commenting API:
      var configJso = {
        'maxDepth': config.maxThreadDepth
      };
      var provider = {
        'id': config.postId,
        'data': items,
        'loadNext': paginator,
        'hasMore': hasMore,
        'getMeta': getMeta,
        'onReply': onReply,
        'rendered': true,
        'initComment': targetComment,
        'initReplyThread': startThread,
        'config': configJso,
        'messages': msgs
      };

      var render = function() {
        if (window.goog && window.goog.comments) {
          var holder = document.getElementById('comment-holder');
          window.goog.comments.render(holder, provider);
        }
      };

      // render now, or queue to render when library loads:
      if (window.goog && window.goog.comments) {
        render();
      } else {
        window.goog = window.goog || {};
        window.goog.comments = window.goog.comments || {};
        window.goog.comments.loadQueue = window.goog.comments.loadQueue || [];
        window.goog.comments.loadQueue.push(render);
      }
    })();
// ]]>
  </script>
</b:includable>
       <b:includable id='threaded_comments' var='post'>
  <div class='comments' id='comments'>
    <a name='comments'/>
    <h4><data:post.commentLabelFull/>:</h4>

    <div class='comments-content'>
      <b:if cond='data:post.embedCommentForm'>
        <b:include data='post' name='threaded_comment_js'/>
      </b:if>
      <div id='comment-holder'>
         <data:post.commentHtml/>
      </div>
    </div>

    <p class='comment-footer'>
      <b:if cond='data:post.allowNewComments'>
        <b:include data='post' name='threaded-comment-form'/>
      <b:else/>
        <data:post.noNewCommentsText/>
      </b:if>
    </p>

    <b:if cond='data:showCmtPopup'>
      <div id='comment-popup'>
        <iframe allowtransparency='true' frameborder='0' id='comment-actions' name='comment-actions' scrolling='no'>
        </iframe>
      </div>
    </b:if>

    <div id='backlinks-container'>
    <div expr:id='data:widget.instanceId + &quot;_backlinks-container&quot;'>
       <b:if cond='data:post.showBacklinks'>
         <b:include data='post' name='backlinks'/>
       </b:if>
    </div>
    </div>
  </div>
</b:includable>
     </b:widget>
     <b:widget id='HTML300' locked='true' title='' type='HTML' version='1'>
       <b:includable id='main'>
          <b:if cond='data:blog.pageType == &quot;item&quot;'>
            <b:if cond='data:content == &quot;blogger&quot;'>
              <div class='comments-system'>
                <div class='blogger-comments'/>
              </div>
            </b:if>
            <b:if cond='data:content == &quot;facebook&quot;'>
              <div class='comments-system'>
                <div class='facebook-comments'/>
              </div>
              <script type='text/javascript'>
              //<![CDATA[
                $('#comments').remove();
              //]]>
              </script>    
            </b:if>
            <b:if cond='data:content == &quot;disqus&quot;'>
              <div class='comments-system'>
                <div id='disqus_thread'/>
              </div>
              <script type='text/javascript'>
              //<![CDATA[
                $('#comments').remove();
              //]]>
              </script>
            </b:if>
            <div id='fb-root'/>&lt;script&gt;$(&quot;.facebook-comments&quot;).append(&quot;&lt;div class=&#39;fb-comments&#39; data-href=&#39;<data:blog.canonicalUrl/>&#39; data-width=&#39;100%&#39; data-numposts=&#39;5&#39; data-colorscheme=&#39;light&#39;&gt;&lt;/div&gt;&quot;);&lt;/script&gt;
          </b:if>
        </b:includable>
     </b:widget>
     <b:widget id='HTML301' locked='true' title='' type='HTML' version='1'>
       <b:includable id='main'>
          <b:if cond='data:blog.pageType == &quot;item&quot;'>
            &lt;script type=&#39;text/javascript&#39;&gt;
            var disqus_shortname = &#39;<data:content/>&#39;;
             (function() {
              var dsq = document.createElement(&#39;script&#39;); dsq.type = &#39;text/javascript&#39;; dsq.async = true;
              dsq.src = &#39;//&#39; + disqus_shortname + &#39;.disqus.com/embed.js&#39;;
              (document.getElementsByTagName(&#39;head&#39;)[0] || document.getElementsByTagName(&#39;body&#39;)[0]).appendChild(dsq);
              })();
            &lt;/script&gt;
          </b:if>
        </b:includable>
     </b:widget>
   </b:section>         

      <b:if cond='data:blog.canonicalUrl == data:blog.canonicalHomepageUrl'>
        <div class='recent-boxes' id='recent-boxes2'> 
          <b:section class='box-sec' id='box-sec2' name='Box Layout 2' showaddelement='yes'>
             <b:widget id='HTML5' locked='false' title='Tennis' type='HTML' version='2' visible='false'>
               <b:widget-settings>
                 <b:widget-setting name='content'><![CDATA[<span data-label="Tennis" id="videos"></span>]]></b:widget-setting>
               </b:widget-settings>
               <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
             </b:widget>
           </b:section>
        </div>
      </b:if>

</div>

   <div id='sidebar-wrapper'>
     <b:section class='sidebar ready-widget' id='sidebar2' name='Sidebar Right A' showaddelement='yes'>
       <b:widget id='LinkList11' locked='false' title='Social Plugin' type='LinkList' version='2' visible='true'>
         <b:widget-settings>
           <b:widget-setting name='sorting'>NONE</b:widget-setting>
           <b:widget-setting name='text-1'>instagram</b:widget-setting>
           <b:widget-setting name='link-1'>https://instagram.com/patilancha_ladka_prince_ganesh?igshid=ZDc4ODBmNjlmNQ==</b:widget-setting>
           <b:widget-setting name='text-0'>facebook</b:widget-setting>
           <b:widget-setting name='link-0'><![CDATA[https://www.facebook.com/profile.php?id=100012722713929&mibextid=D4KYlr]]></b:widget-setting>
         </b:widget-settings>
         <b:includable id='main'>

<b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
   <b:include name='quickedit'/>
 </div>
</b:includable>
         <b:includable id='content'>
 <div class='widget-content'>
   <ul>
     <b:loop values='data:links' var='link'>
       <li><a expr:href='data:link.target'><data:link.name/></a></li>
     </b:loop>
   </ul>
 </div>
</b:includable>
       </b:widget>
       <b:widget id='BlogArchive1' locked='false' title='Blog Archive' type='BlogArchive' version='2' visible='false'>
         <b:widget-settings>
           <b:widget-setting name='showStyle'>HIERARCHY</b:widget-setting>
           <b:widget-setting name='yearPattern'>yyyy</b:widget-setting>
           <b:widget-setting name='showWeekEnd'>true</b:widget-setting>
           <b:widget-setting name='monthPattern'>MMMM yyyy</b:widget-setting>
           <b:widget-setting name='dayPattern'>MMM dd</b:widget-setting>
           <b:widget-setting name='weekPattern'>MM/dd</b:widget-setting>
           <b:widget-setting name='chronological'>false</b:widget-setting>
           <b:widget-setting name='showPosts'>true</b:widget-setting>
           <b:widget-setting name='frequency'>MONTHLY</b:widget-setting>
         </b:widget-settings>
         <b:includable id='main'>
  <b:if cond='data:title != &quot;&quot;'>
    <h2><data:title/></h2>
  </b:if>
  <div class='widget-content'>
  <div id='ArchiveList'>
  <div expr:id='data:widget.instanceId + &quot;_ArchiveList&quot;'>
    <b:include cond='data:style == &quot;HIERARCHY&quot;' data='data' name='interval'/>
    <b:include cond='data:style == &quot;FLAT&quot;' data='data' name='flat'/>
    <b:include cond='data:style == &quot;MENU&quot;' data='data' name='menu'/>
  </div>
  </div>
  <b:include name='quickedit'/>
  </div>
</b:includable>
         <b:includable id='content'>
  <div class='widget-content'>
    <div id='ArchiveList'>
      <div expr:id='data:widget.instanceId + &quot;_ArchiveList&quot;'>
        <b:include cond='data:this.style == &quot;HIERARCHY&quot;' name='hierarchy'/>
        <b:include cond='data:this.style in {&quot;FLAT&quot;, &quot;MENU&quot;}' name='flat'/>
      </div>
    </div>
  </div>
</b:includable>
         <b:includable id='flat' var='data'>
  <ul class='flat'>
    <b:loop values='data:data' var='i'>
      <li class='archivedate'>
        <a expr:href='data:i.url'><data:i.name/></a> (<data:i.post-count/>)
      </li>
    </b:loop>
  </ul>
</b:includable>
         <b:includable id='hierarchy'>
  <b:include data='data' name='interval'/>
</b:includable>
         <b:includable id='interval' var='intervalData'>
  <b:loop values='data:intervalData' var='interval'>
    <ul class='hierarchy'>
      <li expr:class='&quot;archivedate &quot; + data:interval.expclass'>
        <b:include cond='data:interval.toggleId' data='interval' name='toggle'/>
        <a class='post-count-link' expr:href='data:interval.url'>
          <data:interval.name/>
        </a>
        <span class='post-count' dir='ltr'>(<data:interval.post-count/>)</span>
        <b:include cond='data:interval.data' data='interval.data' name='interval'/>
        <b:include cond='data:interval.posts' data='interval.posts' name='posts'/>
      </li>
    </ul>
  </b:loop>
</b:includable>
         <b:includable id='menu' var='data'>
  <select expr:id='data:widget.instanceId + &quot;_ArchiveMenu&quot;'>
    <option value=''><data:title/></option>
    <b:loop values='data:data' var='i'>
      <option expr:value='data:i.url'><data:i.name/> (<data:i.post-count/>)</option>
    </b:loop>
  </select>
</b:includable>
         <b:includable id='posts' var='posts'>
  <ul class='posts'>
    <b:loop values='data:posts' var='post'>
      <li><a expr:href='data:post.url'><data:post.title/></a></li>
    </b:loop>
  </ul>
</b:includable>
         <b:includable id='toggle' var='interval'>
  <a class='toggle' href='javascript:void(0)'>
    <span expr:class='&quot;zippy&quot; + (data:interval.expclass == &quot;expanded&quot; ? &quot; toggle-open&quot; : &quot;&quot;)'>
      <b:if cond='data:interval.expclass == &quot;expanded&quot;'>
        &#9660;&#160;
      <b:elseif cond='data:blog.languageDirection == &quot;rtl&quot;'/>
        &#9668;&#160;
      <b:else/>
        &#9658;&#160;
      </b:if>
    </span>
  </a>
</b:includable>
       </b:widget>
     </b:section>

      </div>
  <div class='clear'/>
    </div>
    <!-- end content-wrapper -->

 <div class='clear'/><!-- Footer wrapper -->


<!-- blocked widgets -->
  <div style='display: none'>
    <b:section class='blocked-widgets' id='blocked-widgets' showaddelement='no' style='display: none'>
      <b:widget id='Attribution1' locked='true' title='' type='Attribution' version='2' visible='true'>
        <b:widget-settings>
          <b:widget-setting name='copyright'/>
        </b:widget-settings>
        <b:includable id='main' var='this'>
  <div class='widget-content'>
    <div class='blogger'>
      <a expr:href='data:bloggerUrl' rel='nofollow'>
        <b:include name='flatBloggerIcon'/>
        <b:message name='messages.poweredByBlogger'/>
      </a>
    </div>

    <b:if cond='data:imageAuthor'>
      <div class='image-attribution'>
        <b:if cond='data:imageAuthor.url'>
          <b:message name='messages.templateImagesByLink'>
            <b:param expr:value='data:imageAuthor.url'/>
            <b:param expr:value='data:imageAuthor.name'/>
          </b:message>
        <b:else/>
          <b:message name='messages.templateImagesBy'>
            <b:param expr:value='data:imageAuthor.name'/>
          </b:message>
        </b:if>
      </div>
    </b:if>

    <b:if cond='data:copyright != &quot;&quot;'>
      <div class='copyright'><data:copyright/></div>
    </b:if>
  </div>
</b:includable>
      </b:widget>
      <b:widget id='Navbar1' locked='true' title='Navbar' type='Navbar' version='1'>
        <b:includable id='main'>&lt;script type=&quot;text/javascript&quot;&gt;
    function setAttributeOnload(object, attribute, val) {
      if(window.addEventListener) {
        window.addEventListener(&#39;load&#39;,
          function(){ object[attribute] = val; }, false);
      } else {
        window.attachEvent(&#39;onload&#39;, function(){ object[attribute] = val; });
      }
    }
  &lt;/script&gt;
&lt;div id=&quot;navbar-iframe-container&quot;&gt;&lt;/div&gt;
&lt;script type=&quot;text/javascript&quot; src=&quot;https://apis.google.com/js/platform.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
      gapi.load(&quot;gapi.iframes:gapi.iframes.style.bubble&quot;, function() {
        if (gapi.iframes &amp;&amp; gapi.iframes.getContext) {
          gapi.iframes.getContext().openChild({
              url: &#39;https://www.blogger.com/navbar.g?targetBlogID\x3d764040363346322776\x26blogName\x3dHealth+with+Ganesh+\x26publishMode\x3dPUBLISH_MODE_HOSTED\x26navbarType\x3dLIGHT\x26layoutType\x3dLAYOUTS\x26searchRoot\x3dhttps://www.healthwithganesh.com/search\x26blogLocale\x3den\x26v\x3d2\x26homepageUrl\x3dhttp://www.healthwithganesh.com/\x26vt\x3d5069919930923590009&#39;,
              where: document.getElementById(&quot;navbar-iframe-container&quot;),
              id: &quot;navbar-iframe&quot;
          });
        }
      });
    &lt;/script&gt;&lt;script type=&quot;text/javascript&quot;&gt;
(function() {
var script = document.createElement(&#39;script&#39;);
script.type = &#39;text/javascript&#39;;
script.src = &#39;//pagead2.googlesyndication.com/pagead/js/google_top_exp.js&#39;;
var head = document.getElementsByTagName(&#39;head&#39;)[0];
if (head) {
head.appendChild(script);
}})();
&lt;/script&gt;
</b:includable>
      </b:widget>
    </b:section>
  </div>

&lt;/div&gt;


<div id='footer-wrapper'> 

   <div class='row' id='footer'>
      <b:section class='sect-left ready-widget' id='footer-sec1' maxwidgets='3' name='Widget 1' showaddelement='yes'>
        <b:widget id='HTML16' locked='false' title='Random Posts' type='HTML' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<span id="randomposts"></span>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
      </b:section>
      <b:section class='sect-left ready-widget' id='footer-sec2' maxwidgets='3' name='Widget 2' showaddelement='yes'>
        <b:widget id='HTML17' locked='false' title='Recent Posts' type='HTML' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<span id="recentposts"></span>]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
        </b:widget>
      </b:section>
      <b:section class='sect-left ready-widget' id='footer-sec3' maxwidgets='3' name='Widget 3' showaddelement='yes'>
        <b:widget id='PopularPosts2' locked='false' title='Popular Posts' type='PopularPosts' version='1'>
          <b:widget-settings>
            <b:widget-setting name='numItemsToShow'>3</b:widget-setting>
            <b:widget-setting name='showThumbnails'>true</b:widget-setting>
            <b:widget-setting name='showSnippets'>true</b:widget-setting>
            <b:widget-setting name='timeRange'>LAST_YEAR</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
  <b:if cond='data:title != &quot;&quot;'><h2><data:title/></h2></b:if>
  <div class='widget-content popular-posts'>
    <ul>
      <b:loop values='data:posts' var='post'>
      <li>
        <b:if cond='!data:showThumbnails'>
          <b:if cond='!data:showSnippets'>
            <!-- (1) No snippet/thumbnail -->
            <a expr:href='data:post.href'><data:post.title/></a>
          <b:else/>
            <!-- (2) Show only snippets -->
            <div class='item-title'><a expr:href='data:post.href'><data:post.title/></a></div>
            <div class='item-snippet'><data:post.snippet/></div>
          </b:if>
        <b:else/>
          <!-- (3) Show only thumbnails or (4) Snippets and thumbnails. -->
          <div expr:class='data:showSnippets ? &quot;item-content&quot; : &quot;item-thumbnail-only&quot;'>
            <b:if cond='data:post.thumbnail'>
              <div class='item-thumbnail'>
                <a expr:href='data:post.href' target='_blank'>
                  <img border='0' expr:alt='data:post.title' expr:height='data:thumbnailSize' expr:src='data:post.thumbnail' expr:width='data:thumbnailSize'/>
                </a>
              </div>
            </b:if>
            <div class='item-title'><a expr:href='data:post.href'><data:post.title/></a></div>
            <b:if cond='data:showSnippets'>
              <div class='item-snippet'><data:post.snippet/></div>
            </b:if>
          </div>
          <div style='clear: both;'/>
        </b:if>
      </li>
      </b:loop>
    </ul>
    <b:include name='quickedit'/>
  </div>
</b:includable>
        </b:widget>
        <b:widget id='LinkList3' locked='false' title='Top menu' type='LinkList' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='link-5'>https://www.healthwithganesh.com/p/privacy-policy.html</b:widget-setting>
            <b:widget-setting name='link-3'>/</b:widget-setting>
            <b:widget-setting name='link-4'>https://www.healthwithganesh.com/p/terms-and-conditions.html</b:widget-setting>
            <b:widget-setting name='text-1'>Contact us</b:widget-setting>
            <b:widget-setting name='text-0'>About Us</b:widget-setting>
            <b:widget-setting name='text-3'>Documentation</b:widget-setting>
            <b:widget-setting name='text-2'>Privacy Policy</b:widget-setting>
            <b:widget-setting name='text-5'>Privacy Policy</b:widget-setting>
            <b:widget-setting name='text-4'>Terms and Conditions</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='link-1'>https://www.pikitemplates.com/?m=1</b:widget-setting>
            <b:widget-setting name='link-2'>https://www.pikitemplates.com/?m=1</b:widget-setting>
            <b:widget-setting name='link-0'>https://www.pikitemplates.com/?m=1</b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
          <b:includable id='content'>
                      <div class='widget-content'>
                        <ul class='nav1'>
                          <b:loop values='data:links' var='link'>
                            <li>
                              <a expr:href='data:link.target'>
                                <data:link.name/>
                              </a>
                            </li>
                          </b:loop>
                        </ul>
                      </div>
                    </b:includable>
        </b:widget>
      </b:section>
  </div>

<div class='clear'/>

<div class='footer-wrapper'>
<div class='footer-copy row'>
<div class='copyright'>Created By <a href='https://www.healthwithganesh.com/'> Health with Ganesh Design By</a> <a href='https://www.healthwithganesh.com/' id='mycontent' ref='dofollow' style='visibility: visible;' title='Blog'>HealthwithGanesh</a>
</div>
<div class='native-opt'>
<li><a class='back-top' href='#top' title='Back to Top'><i class='fa fa-caret-up'/></a></li>
</div>
</div>
</div>
</div>

<script>
//<![CDATA[
/**
 * Owl carousel
 * @version 2.0.0
 * @author Bartosz Wojciechowski
 * @license The MIT License (MIT)
 * @todo Lazy Load Icon
 * @todo prevent animationend bubling
 * @todo itemsScaleUp
 * @todo Test Zepto
 * @todo stagePadding calculate wrong active classes
 */

!function(a,b,c,d){function e(b,c){this.settings=null,this.options=a.extend({},e.Defaults,c),this.$element=a(b),this.drag=a.extend({},m),this.state=a.extend({},n),this.e=a.extend({},o),this._plugins={},this._supress={},this._current=null,this._speed=null,this._coordinates=[],this._breakpoint=null,this._width=null,this._items=[],this._clones=[],this._mergers=[],this._invalidated={},this._pipe=[],a.each(e.Plugins,a.proxy(function(a,b){this._plugins[a[0].toLowerCase()+a.slice(1)]=new b(this)},this)),a.each(e.Pipe,a.proxy(function(b,c){this._pipe.push({filter:c.filter,run:a.proxy(c.run,this)})},this)),this.setup(),this.initialize()}function f(a){if(a.touches!==d)return{x:a.touches[0].pageX,y:a.touches[0].pageY};if(a.touches===d){if(a.pageX!==d)return{x:a.pageX,y:a.pageY};if(a.pageX===d)return{x:a.clientX,y:a.clientY}}}function g(a){var b,d,e=c.createElement("div"),f=a;for(b in f)if(d=f[b],"undefined"!=typeof e.style[d])return e=null,[d,b];return[!1]}function h(){return g(["transition","WebkitTransition","MozTransition","OTransition"])[1]}function i(){return g(["transform","WebkitTransform","MozTransform","OTransform","msTransform"])[0]}function j(){return g(["perspective","webkitPerspective","MozPerspective","OPerspective","MsPerspective"])[0]}function k(){return"ontouchstart"in b||!!navigator.msMaxTouchPoints}function l(){return b.navigator.msPointerEnabled}var m,n,o;m={start:0,startX:0,startY:0,current:0,currentX:0,currentY:0,offsetX:0,offsetY:0,distance:null,startTime:0,endTime:0,updatedX:0,targetEl:null},n={isTouch:!1,isScrolling:!1,isSwiping:!1,direction:!1,inMotion:!1},o={_onDragStart:null,_onDragMove:null,_onDragEnd:null,_transitionEnd:null,_resizer:null,_responsiveCall:null,_goToLoop:null,_checkVisibile:null},e.Defaults={items:3,loop:!1,center:!1,mouseDrag:!0,touchDrag:!0,pullDrag:!0,freeDrag:!1,margin:0,stagePadding:0,merge:!1,mergeFit:!0,autoWidth:!1,startPosition:0,rtl:!1,smartSpeed:250,fluidSpeed:!1,dragEndSpeed:!1,responsive:{},responsiveRefreshRate:200,responsiveBaseElement:b,responsiveClass:!1,fallbackEasing:"swing",info:!1,nestedItemSelector:!1,itemElement:"div",stageElement:"div",themeClass:"owl-theme",baseClass:"owl-carousel",itemClass:"owl-item",centerClass:"center",activeClass:"active"},e.Width={Default:"default",Inner:"inner",Outer:"outer"},e.Plugins={},e.Pipe=[{filter:["width","items","settings"],run:function(a){a.current=this._items&&this._items[this.relative(this._current)]}},{filter:["items","settings"],run:function(){var a=this._clones,b=this.$stage.children(".cloned");(b.length!==a.length||!this.settings.loop&&a.length>0)&&(this.$stage.children(".cloned").remove(),this._clones=[])}},{filter:["items","settings"],run:function(){var a,b,c=this._clones,d=this._items,e=this.settings.loop?c.length-Math.max(2*this.settings.items,4):0;for(a=0,b=Math.abs(e/2);b>a;a++)e>0?(this.$stage.children().eq(d.length+c.length-1).remove(),c.pop(),this.$stage.children().eq(0).remove(),c.pop()):(c.push(c.length/2),this.$stage.append(d[c[c.length-1]].clone().addClass("cloned")),c.push(d.length-1-(c.length-1)/2),this.$stage.prepend(d[c[c.length-1]].clone().addClass("cloned")))}},{filter:["width","items","settings"],run:function(){var a,b,c,d=this.settings.rtl?1:-1,e=(this.width()/this.settings.items).toFixed(3),f=0;for(this._coordinates=[],b=0,c=this._clones.length+this._items.length;c>b;b++)a=this._mergers[this.relative(b)],a=this.settings.mergeFit&&Math.min(a,this.settings.items)||a,f+=(this.settings.autoWidth?this._items[this.relative(b)].width()+this.settings.margin:e*a)*d,this._coordinates.push(f)}},{filter:["width","items","settings"],run:function(){var b,c,d=(this.width()/this.settings.items).toFixed(3),e={width:Math.abs(this._coordinates[this._coordinates.length-1])+2*this.settings.stagePadding,"padding-left":this.settings.stagePadding||"","padding-right":this.settings.stagePadding||""};if(this.$stage.css(e),e={width:this.settings.autoWidth?"auto":d-this.settings.margin},e[this.settings.rtl?"margin-left":"margin-right"]=this.settings.margin,!this.settings.autoWidth&&a.grep(this._mergers,function(a){return a>1}).length>0)for(b=0,c=this._coordinates.length;c>b;b++)e.width=Math.abs(this._coordinates[b])-Math.abs(this._coordinates[b-1]||0)-this.settings.margin,this.$stage.children().eq(b).css(e);else this.$stage.children().css(e)}},{filter:["width","items","settings"],run:function(a){a.current&&this.reset(this.$stage.children().index(a.current))}},{filter:["position"],run:function(){this.animate(this.coordinates(this._current))}},{filter:["width","position","items","settings"],run:function(){var a,b,c,d,e=this.settings.rtl?1:-1,f=2*this.settings.stagePadding,g=this.coordinates(this.current())+f,h=g+this.width()*e,i=[];for(c=0,d=this._coordinates.length;d>c;c++)a=this._coordinates[c-1]||0,b=Math.abs(this._coordinates[c])+f*e,(this.op(a,"<=",g)&&this.op(a,">",h)||this.op(b,"<",g)&&this.op(b,">",h))&&i.push(c);this.$stage.children("."+this.settings.activeClass).removeClass(this.settings.activeClass),this.$stage.children(":eq("+i.join("), :eq(")+")").addClass(this.settings.activeClass),this.settings.center&&(this.$stage.children("."+this.settings.centerClass).removeClass(this.settings.centerClass),this.$stage.children().eq(this.current()).addClass(this.settings.centerClass))}}],e.prototype.initialize=function(){if(this.trigger("initialize"),this.$element.addClass(this.settings.baseClass).addClass(this.settings.themeClass).toggleClass("owl-rtl",this.settings.rtl),this.browserSupport(),this.settings.autoWidth&&this.state.imagesLoaded!==!0){var b,c,e;if(b=this.$element.find("img"),c=this.settings.nestedItemSelector?"."+this.settings.nestedItemSelector:d,e=this.$element.children(c).width(),b.length&&0>=e)return this.preloadAutoWidthImages(b),!1}this.$element.addClass("owl-loading"),this.$stage=a("<"+this.settings.stageElement+' class="owl-stage"/>').wrap('<div class="owl-stage-outer">'),this.$element.append(this.$stage.parent()),this.replace(this.$element.children().not(this.$stage.parent())),this._width=this.$element.width(),this.refresh(),this.$element.removeClass("owl-loading").addClass("owl-loaded"),this.eventsCall(),this.internalEvents(),this.addTriggerableEvents(),this.trigger("initialized")},e.prototype.setup=function(){var b=this.viewport(),c=this.options.responsive,d=-1,e=null;c?(a.each(c,function(a){b>=a&&a>d&&(d=Number(a))}),e=a.extend({},this.options,c[d]),delete e.responsive,e.responsiveClass&&this.$element.attr("class",function(a,b){return b.replace(/\b owl-responsive-\S+/g,"")}).addClass("owl-responsive-"+d)):e=a.extend({},this.options),(null===this.settings||this._breakpoint!==d)&&(this.trigger("change",{property:{name:"settings",value:e}}),this._breakpoint=d,this.settings=e,this.invalidate("settings"),this.trigger("changed",{property:{name:"settings",value:this.settings}}))},e.prototype.optionsLogic=function(){this.$element.toggleClass("owl-center",this.settings.center),this.settings.loop&&this._items.length<this.settings.items&&(this.settings.loop=!1),this.settings.autoWidth&&(this.settings.stagePadding=!1,this.settings.merge=!1)},e.prototype.prepare=function(b){var c=this.trigger("prepare",{content:b});return c.data||(c.data=a("<"+this.settings.itemElement+"/>").addClass(this.settings.itemClass).append(b)),this.trigger("prepared",{content:c.data}),c.data},e.prototype.update=function(){for(var b=0,c=this._pipe.length,d=a.proxy(function(a){return this[a]},this._invalidated),e={};c>b;)(this._invalidated.all||a.grep(this._pipe[b].filter,d).length>0)&&this._pipe[b].run(e),b++;this._invalidated={}},e.prototype.width=function(a){switch(a=a||e.Width.Default){case e.Width.Inner:case e.Width.Outer:return this._width;default:return this._width-2*this.settings.stagePadding+this.settings.margin}},e.prototype.refresh=function(){if(0===this._items.length)return!1;(new Date).getTime();this.trigger("refresh"),this.setup(),this.optionsLogic(),this.$stage.addClass("owl-refresh"),this.update(),this.$stage.removeClass("owl-refresh"),this.state.orientation=b.orientation,this.watchVisibility(),this.trigger("refreshed")},e.prototype.eventsCall=function(){this.e._onDragStart=a.proxy(function(a){this.onDragStart(a)},this),this.e._onDragMove=a.proxy(function(a){this.onDragMove(a)},this),this.e._onDragEnd=a.proxy(function(a){this.onDragEnd(a)},this),this.e._onResize=a.proxy(function(a){this.onResize(a)},this),this.e._transitionEnd=a.proxy(function(a){this.transitionEnd(a)},this),this.e._preventClick=a.proxy(function(a){this.preventClick(a)},this)},e.prototype.onThrottledResize=function(){b.clearTimeout(this.resizeTimer),this.resizeTimer=b.setTimeout(this.e._onResize,this.settings.responsiveRefreshRate)},e.prototype.onResize=function(){return this._items.length?this._width===this.$element.width()?!1:this.trigger("resize").isDefaultPrevented()?!1:(this._width=this.$element.width(),this.invalidate("width"),this.refresh(),void this.trigger("resized")):!1},e.prototype.eventsRouter=function(a){var b=a.type;"mousedown"===b||"touchstart"===b?this.onDragStart(a):"mousemove"===b||"touchmove"===b?this.onDragMove(a):"mouseup"===b||"touchend"===b?this.onDragEnd(a):"touchcancel"===b&&this.onDragEnd(a)},e.prototype.internalEvents=function(){var c=(k(),l());this.settings.mouseDrag?(this.$stage.on("mousedown",a.proxy(function(a){this.eventsRouter(a)},this)),this.$stage.on("dragstart",function(){return!1}),this.$stage.get(0).onselectstart=function(){return!1}):this.$element.addClass("owl-text-select-on"),this.settings.touchDrag&&!c&&this.$stage.on("touchstart touchcancel",a.proxy(function(a){this.eventsRouter(a)},this)),this.transitionEndVendor&&this.on(this.$stage.get(0),this.transitionEndVendor,this.e._transitionEnd,!1),this.settings.responsive!==!1&&this.on(b,"resize",a.proxy(this.onThrottledResize,this))},e.prototype.onDragStart=function(d){var e,g,h,i;if(e=d.originalEvent||d||b.event,3===e.which||this.state.isTouch)return!1;if("mousedown"===e.type&&this.$stage.addClass("owl-grab"),this.trigger("drag"),this.drag.startTime=(new Date).getTime(),this.speed(0),this.state.isTouch=!0,this.state.isScrolling=!1,this.state.isSwiping=!1,this.drag.distance=0,g=f(e).x,h=f(e).y,this.drag.offsetX=this.$stage.position().left,this.drag.offsetY=this.$stage.position().top,this.settings.rtl&&(this.drag.offsetX=this.$stage.position().left+this.$stage.width()-this.width()+this.settings.margin),this.state.inMotion&&this.support3d)i=this.getTransformProperty(),this.drag.offsetX=i,this.animate(i),this.state.inMotion=!0;else if(this.state.inMotion&&!this.support3d)return this.state.inMotion=!1,!1;this.drag.startX=g-this.drag.offsetX,this.drag.startY=h-this.drag.offsetY,this.drag.start=g-this.drag.startX,this.drag.targetEl=e.target||e.srcElement,this.drag.updatedX=this.drag.start,("IMG"===this.drag.targetEl.tagName||"A"===this.drag.targetEl.tagName)&&(this.drag.targetEl.draggable=!1),a(c).on("mousemove.owl.dragEvents mouseup.owl.dragEvents touchmove.owl.dragEvents touchend.owl.dragEvents",a.proxy(function(a){this.eventsRouter(a)},this))},e.prototype.onDragMove=function(a){var c,e,g,h,i,j;this.state.isTouch&&(this.state.isScrolling||(c=a.originalEvent||a||b.event,e=f(c).x,g=f(c).y,this.drag.currentX=e-this.drag.startX,this.drag.currentY=g-this.drag.startY,this.drag.distance=this.drag.currentX-this.drag.offsetX,this.drag.distance<0?this.state.direction=this.settings.rtl?"right":"left":this.drag.distance>0&&(this.state.direction=this.settings.rtl?"left":"right"),this.settings.loop?this.op(this.drag.currentX,">",this.coordinates(this.minimum()))&&"right"===this.state.direction?this.drag.currentX-=(this.settings.center&&this.coordinates(0))-this.coordinates(this._items.length):this.op(this.drag.currentX,"<",this.coordinates(this.maximum()))&&"left"===this.state.direction&&(this.drag.currentX+=(this.settings.center&&this.coordinates(0))-this.coordinates(this._items.length)):(h=this.coordinates(this.settings.rtl?this.maximum():this.minimum()),i=this.coordinates(this.settings.rtl?this.minimum():this.maximum()),j=this.settings.pullDrag?this.drag.distance/5:0,this.drag.currentX=Math.max(Math.min(this.drag.currentX,h+j),i+j)),(this.drag.distance>8||this.drag.distance<-8)&&(c.preventDefault!==d?c.preventDefault():c.returnValue=!1,this.state.isSwiping=!0),this.drag.updatedX=this.drag.currentX,(this.drag.currentY>16||this.drag.currentY<-16)&&this.state.isSwiping===!1&&(this.state.isScrolling=!0,this.drag.updatedX=this.drag.start),this.animate(this.drag.updatedX)))},e.prototype.onDragEnd=function(b){var d,e,f;if(this.state.isTouch){if("mouseup"===b.type&&this.$stage.removeClass("owl-grab"),this.trigger("dragged"),this.drag.targetEl.removeAttribute("draggable"),this.state.isTouch=!1,this.state.isScrolling=!1,this.state.isSwiping=!1,0===this.drag.distance&&this.state.inMotion!==!0)return this.state.inMotion=!1,!1;this.drag.endTime=(new Date).getTime(),d=this.drag.endTime-this.drag.startTime,e=Math.abs(this.drag.distance),(e>3||d>300)&&this.removeClick(this.drag.targetEl),f=this.closest(this.drag.updatedX),this.speed(this.settings.dragEndSpeed||this.settings.smartSpeed),this.current(f),this.invalidate("position"),this.update(),this.settings.pullDrag||this.drag.updatedX!==this.coordinates(f)||this.transitionEnd(),this.drag.distance=0,a(c).off(".owl.dragEvents")}},e.prototype.removeClick=function(c){this.drag.targetEl=c,a(c).on("click.preventClick",this.e._preventClick),b.setTimeout(function(){a(c).off("click.preventClick")},300)},e.prototype.preventClick=function(b){b.preventDefault?b.preventDefault():b.returnValue=!1,b.stopPropagation&&b.stopPropagation(),a(b.target).off("click.preventClick")},e.prototype.getTransformProperty=function(){var a,c;return a=b.getComputedStyle(this.$stage.get(0),null).getPropertyValue(this.vendorName+"transform"),a=a.replace(/matrix(3d)?\(|\)/g,"").split(","),c=16===a.length,c!==!0?a[4]:a[12]},e.prototype.closest=function(b){var c=-1,d=30,e=this.width(),f=this.coordinates();return this.settings.freeDrag||a.each(f,a.proxy(function(a,g){return b>g-d&&g+d>b?c=a:this.op(b,"<",g)&&this.op(b,">",f[a+1]||g-e)&&(c="left"===this.state.direction?a+1:a),-1===c},this)),this.settings.loop||(this.op(b,">",f[this.minimum()])?c=b=this.minimum():this.op(b,"<",f[this.maximum()])&&(c=b=this.maximum())),c},e.prototype.animate=function(b){this.trigger("translate"),this.state.inMotion=this.speed()>0,this.support3d?this.$stage.css({transform:"translate3d("+b+"px,0px, 0px)",transition:this.speed()/1e3+"s"}):this.state.isTouch?this.$stage.css({left:b+"px"}):this.$stage.animate({left:b},this.speed()/1e3,this.settings.fallbackEasing,a.proxy(function(){this.state.inMotion&&this.transitionEnd()},this))},e.prototype.current=function(a){if(a===d)return this._current;if(0===this._items.length)return d;if(a=this.normalize(a),this._current!==a){var b=this.trigger("change",{property:{name:"position",value:a}});b.data!==d&&(a=this.normalize(b.data)),this._current=a,this.invalidate("position"),this.trigger("changed",{property:{name:"position",value:this._current}})}return this._current},e.prototype.invalidate=function(a){this._invalidated[a]=!0},e.prototype.reset=function(a){a=this.normalize(a),a!==d&&(this._speed=0,this._current=a,this.suppress(["translate","translated"]),this.animate(this.coordinates(a)),this.release(["translate","translated"]))},e.prototype.normalize=function(b,c){var e=c?this._items.length:this._items.length+this._clones.length;return!a.isNumeric(b)||1>e?d:b=this._clones.length?(b%e+e)%e:Math.max(this.minimum(c),Math.min(this.maximum(c),b))},e.prototype.relative=function(a){return a=this.normalize(a),a-=this._clones.length/2,this.normalize(a,!0)},e.prototype.maximum=function(a){var b,c,d,e=0,f=this.settings;if(a)return this._items.length-1;if(!f.loop&&f.center)b=this._items.length-1;else if(f.loop||f.center)if(f.loop||f.center)b=this._items.length+f.items;else{if(!f.autoWidth&&!f.merge)throw"Can not detect maximum absolute position.";for(revert=f.rtl?1:-1,c=this.$stage.width()-this.$element.width();(d=this.coordinates(e))&&!(d*revert>=c);)b=++e}else b=this._items.length-f.items;return b},e.prototype.minimum=function(a){return a?0:this._clones.length/2},e.prototype.items=function(a){return a===d?this._items.slice():(a=this.normalize(a,!0),this._items[a])},e.prototype.mergers=function(a){return a===d?this._mergers.slice():(a=this.normalize(a,!0),this._mergers[a])},e.prototype.clones=function(b){var c=this._clones.length/2,e=c+this._items.length,f=function(a){return a%2===0?e+a/2:c-(a+1)/2};return b===d?a.map(this._clones,function(a,b){return f(b)}):a.map(this._clones,function(a,c){return a===b?f(c):null})},e.prototype.speed=function(a){return a!==d&&(this._speed=a),this._speed},e.prototype.coordinates=function(b){var c=null;return b===d?a.map(this._coordinates,a.proxy(function(a,b){return this.coordinates(b)},this)):(this.settings.center?(c=this._coordinates[b],c+=(this.width()-c+(this._coordinates[b-1]||0))/2*(this.settings.rtl?-1:1)):c=this._coordinates[b-1]||0,c)},e.prototype.duration=function(a,b,c){return Math.min(Math.max(Math.abs(b-a),1),6)*Math.abs(c||this.settings.smartSpeed)},e.prototype.to=function(c,d){if(this.settings.loop){var e=c-this.relative(this.current()),f=this.current(),g=this.current(),h=this.current()+e,i=0>g-h?!0:!1,j=this._clones.length+this._items.length;h<this.settings.items&&i===!1?(f=g+this._items.length,this.reset(f)):h>=j-this.settings.items&&i===!0&&(f=g-this._items.length,this.reset(f)),b.clearTimeout(this.e._goToLoop),this.e._goToLoop=b.setTimeout(a.proxy(function(){this.speed(this.duration(this.current(),f+e,d)),this.current(f+e),this.update()},this),30)}else this.speed(this.duration(this.current(),c,d)),this.current(c),this.update()},e.prototype.next=function(a){a=a||!1,this.to(this.relative(this.current())+1,a)},e.prototype.prev=function(a){a=a||!1,this.to(this.relative(this.current())-1,a)},e.prototype.transitionEnd=function(a){return a!==d&&(a.stopPropagation(),(a.target||a.srcElement||a.originalTarget)!==this.$stage.get(0))?!1:(this.state.inMotion=!1,void this.trigger("translated"))},e.prototype.viewport=function(){var d;if(this.options.responsiveBaseElement!==b)d=a(this.options.responsiveBaseElement).width();else if(b.innerWidth)d=b.innerWidth;else{if(!c.documentElement||!c.documentElement.clientWidth)throw"Can not detect viewport width.";d=c.documentElement.clientWidth}return d},e.prototype.replace=function(b){this.$stage.empty(),this._items=[],b&&(b=b instanceof jQuery?b:a(b)),this.settings.nestedItemSelector&&(b=b.find("."+this.settings.nestedItemSelector)),b.filter(function(){return 1===this.nodeType}).each(a.proxy(function(a,b){b=this.prepare(b),this.$stage.append(b),this._items.push(b),this._mergers.push(1*b.find("[data-merge]").andSelf("[data-merge]").attr("data-merge")||1)},this)),this.reset(a.isNumeric(this.settings.startPosition)?this.settings.startPosition:0),this.invalidate("items")},e.prototype.add=function(a,b){b=b===d?this._items.length:this.normalize(b,!0),this.trigger("add",{content:a,position:b}),0===this._items.length||b===this._items.length?(this.$stage.append(a),this._items.push(a),this._mergers.push(1*a.find("[data-merge]").andSelf("[data-merge]").attr("data-merge")||1)):(this._items[b].before(a),this._items.splice(b,0,a),this._mergers.splice(b,0,1*a.find("[data-merge]").andSelf("[data-merge]").attr("data-merge")||1)),this.invalidate("items"),this.trigger("added",{content:a,position:b})},e.prototype.remove=function(a){a=this.normalize(a,!0),a!==d&&(this.trigger("remove",{content:this._items[a],position:a}),this._items[a].remove(),this._items.splice(a,1),this._mergers.splice(a,1),this.invalidate("items"),this.trigger("removed",{content:null,position:a}))},e.prototype.addTriggerableEvents=function(){var b=a.proxy(function(b,c){return a.proxy(function(a){a.relatedTarget!==this&&(this.suppress([c]),b.apply(this,[].slice.call(arguments,1)),this.release([c]))},this)},this);a.each({next:this.next,prev:this.prev,to:this.to,destroy:this.destroy,refresh:this.refresh,replace:this.replace,add:this.add,remove:this.remove},a.proxy(function(a,c){this.$element.on(a+".owl.carousel",b(c,a+".owl.carousel"))},this))},e.prototype.watchVisibility=function(){function c(a){return a.offsetWidth>0&&a.offsetHeight>0}function d(){c(this.$element.get(0))&&(this.$element.removeClass("owl-hidden"),this.refresh(),b.clearInterval(this.e._checkVisibile))}c(this.$element.get(0))||(this.$element.addClass("owl-hidden"),b.clearInterval(this.e._checkVisibile),this.e._checkVisibile=b.setInterval(a.proxy(d,this),500))},e.prototype.preloadAutoWidthImages=function(b){var c,d,e,f;c=0,d=this,b.each(function(g,h){e=a(h),f=new Image,f.onload=function(){c++,e.attr("src",f.src),e.css("opacity",1),c>=b.length&&(d.state.imagesLoaded=!0,d.initialize())},f.src=e.attr("src")||e.attr("data-src")||e.attr("data-src-retina")})},e.prototype.destroy=function(){this.$element.hasClass(this.settings.themeClass)&&this.$element.removeClass(this.settings.themeClass),this.settings.responsive!==!1&&a(b).off("resize.owl.carousel"),this.transitionEndVendor&&this.off(this.$stage.get(0),this.transitionEndVendor,this.e._transitionEnd);for(var d in this._plugins)this._plugins[d].destroy();(this.settings.mouseDrag||this.settings.touchDrag)&&(this.$stage.off("mousedown touchstart touchcancel"),a(c).off(".owl.dragEvents"),this.$stage.get(0).onselectstart=function(){},this.$stage.off("dragstart",function(){return!1})),this.$element.off(".owl"),this.$stage.children(".cloned").remove(),this.e=null,this.$element.removeData("owlCarousel"),this.$stage.children().contents().unwrap(),this.$stage.children().unwrap(),this.$stage.unwrap()},e.prototype.op=function(a,b,c){var d=this.settings.rtl;switch(b){case"<":return d?a>c:c>a;case">":return d?c>a:a>c;case">=":return d?c>=a:a>=c;case"<=":return d?a>=c:c>=a}},e.prototype.on=function(a,b,c,d){a.addEventListener?a.addEventListener(b,c,d):a.attachEvent&&a.attachEvent("on"+b,c)},e.prototype.off=function(a,b,c,d){a.removeEventListener?a.removeEventListener(b,c,d):a.detachEvent&&a.detachEvent("on"+b,c)},e.prototype.trigger=function(b,c,d){var e={item:{count:this._items.length,index:this.current()}},f=a.camelCase(a.grep(["on",b,d],function(a){return a}).join("-").toLowerCase()),g=a.Event([b,"owl",d||"carousel"].join(".").toLowerCase(),a.extend({relatedTarget:this},e,c));return this._supress[b]||(a.each(this._plugins,function(a,b){b.onTrigger&&b.onTrigger(g)}),this.$element.trigger(g),this.settings&&"function"==typeof this.settings[f]&&this.settings[f].apply(this,g)),g},e.prototype.suppress=function(b){a.each(b,a.proxy(function(a,b){this._supress[b]=!0},this))},e.prototype.release=function(b){a.each(b,a.proxy(function(a,b){delete this._supress[b]},this))},e.prototype.browserSupport=function(){if(this.support3d=j(),this.support3d){this.transformVendor=i();var a=["transitionend","webkitTransitionEnd","transitionend","oTransitionEnd"];this.transitionEndVendor=a[h()],this.vendorName=this.transformVendor.replace(/Transform/i,""),this.vendorName=""!==this.vendorName?"-"+this.vendorName.toLowerCase()+"-":""}this.state.orientation=b.orientation},a.fn.owlCarousel=function(b){return this.each(function(){a(this).data("owlCarousel")||a(this).data("owlCarousel",new e(this,b))})},a.fn.owlCarousel.Constructor=e}(window.Zepto||window.jQuery,window,document),function(a,b){var c=function(b){this._core=b,this._loaded=[],this._handlers={"initialized.owl.carousel change.owl.carousel":a.proxy(function(b){if(b.namespace&&this._core.settings&&this._core.settings.lazyLoad&&(b.property&&"position"==b.property.name||"initialized"==b.type))for(var c=this._core.settings,d=c.center&&Math.ceil(c.items/2)||c.items,e=c.center&&-1*d||0,f=(b.property&&b.property.value||this._core.current())+e,g=this._core.clones().length,h=a.proxy(function(a,b){this.load(b)},this);e++<d;)this.load(g/2+this._core.relative(f)),g&&a.each(this._core.clones(this._core.relative(f++)),h)},this)},this._core.options=a.extend({},c.Defaults,this._core.options),this._core.$element.on(this._handlers)};c.Defaults={lazyLoad:!1},c.prototype.load=function(c){var d=this._core.$stage.children().eq(c),e=d&&d.find(".owl-lazy");!e||a.inArray(d.get(0),this._loaded)>-1||(e.each(a.proxy(function(c,d){var e,f=a(d),g=b.devicePixelRatio>1&&f.attr("data-src-retina")||f.attr("data-src");this._core.trigger("load",{element:f,url:g},"lazy"),f.is("img")?f.one("load.owl.lazy",a.proxy(function(){f.css("opacity",1),this._core.trigger("loaded",{element:f,url:g},"lazy")},this)).attr("src",g):(e=new Image,e.onload=a.proxy(function(){f.css({"background-image":"url("+g+")",opacity:"1"}),this._core.trigger("loaded",{element:f,url:g},"lazy")},this),e.src=g)},this)),this._loaded.push(d.get(0)))},c.prototype.destroy=function(){var a,b;for(a in this.handlers)this._core.$element.off(a,this.handlers[a]);for(b in Object.getOwnPropertyNames(this))"function"!=typeof this[b]&&(this[b]=null)},a.fn.owlCarousel.Constructor.Plugins.Lazy=c}(window.Zepto||window.jQuery,window,document),function(a){var b=function(c){this._core=c,this._handlers={"initialized.owl.carousel":a.proxy(function(){this._core.settings.autoHeight&&this.update()},this),"changed.owl.carousel":a.proxy(function(a){this._core.settings.autoHeight&&"position"==a.property.name&&this.update()},this),"loaded.owl.lazy":a.proxy(function(a){this._core.settings.autoHeight&&a.element.closest("."+this._core.settings.itemClass)===this._core.$stage.children().eq(this._core.current())&&this.update()},this)},this._core.options=a.extend({},b.Defaults,this._core.options),this._core.$element.on(this._handlers)};b.Defaults={autoHeight:!1,autoHeightClass:"owl-height"},b.prototype.update=function(){this._core.$stage.parent().height(this._core.$stage.children().eq(this._core.current()).height()).addClass(this._core.settings.autoHeightClass)},b.prototype.destroy=function(){var a,b;for(a in this._handlers)this._core.$element.off(a,this._handlers[a]);for(b in Object.getOwnPropertyNames(this))"function"!=typeof this[b]&&(this[b]=null)},a.fn.owlCarousel.Constructor.Plugins.AutoHeight=b}(window.Zepto||window.jQuery,window,document),function(a,b,c){var d=function(b){this._core=b,this._videos={},this._playing=null,this._fullscreen=!1,this._handlers={"resize.owl.carousel":a.proxy(function(a){this._core.settings.video&&!this.isInFullScreen()&&a.preventDefault()},this),"refresh.owl.carousel changed.owl.carousel":a.proxy(function(){this._playing&&this.stop()},this),"prepared.owl.carousel":a.proxy(function(b){var c=a(b.content).find(".owl-video");c.length&&(c.css("display","none"),this.fetch(c,a(b.content)))},this)},this._core.options=a.extend({},d.Defaults,this._core.options),this._core.$element.on(this._handlers),this._core.$element.on("click.owl.video",".owl-video-play-icon",a.proxy(function(a){this.play(a)},this))};d.Defaults={video:!1,videoHeight:!1,videoWidth:!1},d.prototype.fetch=function(a,b){var c=a.attr("data-vimeo-id")?"vimeo":"youtube",d=a.attr("data-vimeo-id")||a.attr("data-youtube-id"),e=a.attr("data-width")||this._core.settings.videoWidth,f=a.attr("data-height")||this._core.settings.videoHeight,g=a.attr("href");if(!g)throw new Error("Missing video URL.");if(d=g.match(/(http:|https:|)\/\/(player.|www.)?(vimeo\.com|youtu(be\.com|\.be|be\.googleapis\.com))\/(video\/|embed\/|watch\?v=|v\/)?([A-Za-z0-9._%-]*)(\&\S+)?/),d[3].indexOf("youtu")>-1)c="youtube";else{if(!(d[3].indexOf("vimeo")>-1))throw new Error("Video URL not supported.");c="vimeo"}d=d[6],this._videos[g]={type:c,id:d,width:e,height:f},b.attr("data-video",g),this.thumbnail(a,this._videos[g])},d.prototype.thumbnail=function(b,c){var d,e,f,g=c.width&&c.height?'style="width:'+c.width+"px;height:"+c.height+'px;"':"",h=b.find("img"),i="src",j="",k=this._core.settings,l=function(a){e='<div class="owl-video-play-icon"></div>',d=k.lazyLoad?'<div class="owl-video-tn '+j+'" '+i+'="'+a+'"></div>':'<div class="owl-video-tn" style="opacity:1;background-image:url('+a+')"></div>',b.after(d),b.after(e)};return b.wrap('<div class="owl-video-wrapper"'+g+"></div>"),this._core.settings.lazyLoad&&(i="data-src",j="owl-lazy"),h.length?(l(h.attr(i)),h.remove(),!1):void("youtube"===c.type?(f="http://img.youtube.com/vi/"+c.id+"/hqdefault.jpg",l(f)):"vimeo"===c.type&&a.ajax({type:"GET",url:"http://vimeo.com/api/v2/video/"+c.id+".json",jsonp:"callback",dataType:"jsonp",success:function(a){f=a[0].thumbnail_large,l(f)}}))},d.prototype.stop=function(){this._core.trigger("stop",null,"video"),this._playing.find(".owl-video-frame").remove(),this._playing.removeClass("owl-video-playing"),this._playing=null},d.prototype.play=function(b){this._core.trigger("play",null,"video"),this._playing&&this.stop();var c,d,e=a(b.target||b.srcElement),f=e.closest("."+this._core.settings.itemClass),g=this._videos[f.attr("data-video")],h=g.width||"100%",i=g.height||this._core.$stage.height();"youtube"===g.type?c='<iframe width="'+h+'" height="'+i+'" src="http://www.youtube.com/embed/'+g.id+"?autoplay=1&v="+g.id+'" frameborder="0" allowfullscreen></iframe>':"vimeo"===g.type&&(c='<iframe src="http://player.vimeo.com/video/'+g.id+'?autoplay=1" width="'+h+'" height="'+i+'" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>'),f.addClass("owl-video-playing"),this._playing=f,d=a('<div style="height:'+i+"px; width:"+h+'px" class="owl-video-frame">'+c+"</div>"),e.after(d)},d.prototype.isInFullScreen=function(){var d=c.fullscreenElement||c.mozFullScreenElement||c.webkitFullscreenElement;return d&&a(d).parent().hasClass("owl-video-frame")&&(this._core.speed(0),this._fullscreen=!0),d&&this._fullscreen&&this._playing?!1:this._fullscreen?(this._fullscreen=!1,!1):this._playing&&this._core.state.orientation!==b.orientation?(this._core.state.orientation=b.orientation,!1):!0},d.prototype.destroy=function(){var a,b;this._core.$element.off("click.owl.video");for(a in this._handlers)this._core.$element.off(a,this._handlers[a]);for(b in Object.getOwnPropertyNames(this))"function"!=typeof this[b]&&(this[b]=null)},a.fn.owlCarousel.Constructor.Plugins.Video=d}(window.Zepto||window.jQuery,window,document),function(a,b,c,d){var e=function(b){this.core=b,this.core.options=a.extend({},e.Defaults,this.core.options),this.swapping=!0,this.previous=d,this.next=d,this.handlers={"change.owl.carousel":a.proxy(function(a){"position"==a.property.name&&(this.previous=this.core.current(),this.next=a.property.value)},this),"drag.owl.carousel dragged.owl.carousel translated.owl.carousel":a.proxy(function(a){this.swapping="translated"==a.type},this),"translate.owl.carousel":a.proxy(function(){this.swapping&&(this.core.options.animateOut||this.core.options.animateIn)&&this.swap()},this)},this.core.$element.on(this.handlers)};e.Defaults={animateOut:!1,animateIn:!1},e.prototype.swap=function(){if(1===this.core.settings.items&&this.core.support3d){this.core.speed(0);var b,c=a.proxy(this.clear,this),d=this.core.$stage.children().eq(this.previous),e=this.core.$stage.children().eq(this.next),f=this.core.settings.animateIn,g=this.core.settings.animateOut;this.core.current()!==this.previous&&(g&&(b=this.core.coordinates(this.previous)-this.core.coordinates(this.next),d.css({left:b+"px"}).addClass("animated owl-animated-out").addClass(g).one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",c)),f&&e.addClass("animated owl-animated-in").addClass(f).one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",c))}},e.prototype.clear=function(b){a(b.target).css({left:""}).removeClass("animated owl-animated-out owl-animated-in").removeClass(this.core.settings.animateIn).removeClass(this.core.settings.animateOut),this.core.transitionEnd()},e.prototype.destroy=function(){var a,b;for(a in this.handlers)this.core.$element.off(a,this.handlers[a]);for(b in Object.getOwnPropertyNames(this))"function"!=typeof this[b]&&(this[b]=null)},a.fn.owlCarousel.Constructor.Plugins.Animate=e}(window.Zepto||window.jQuery,window,document),function(a,b,c){var d=function(b){this.core=b,this.core.options=a.extend({},d.Defaults,this.core.options),this.handlers={"translated.owl.carousel refreshed.owl.carousel":a.proxy(function(){this.autoplay()
},this),"play.owl.autoplay":a.proxy(function(a,b,c){this.play(b,c)},this),"stop.owl.autoplay":a.proxy(function(){this.stop()},this),"mouseover.owl.autoplay":a.proxy(function(){this.core.settings.autoplayHoverPause&&this.pause()},this),"mouseleave.owl.autoplay":a.proxy(function(){this.core.settings.autoplayHoverPause&&this.autoplay()},this)},this.core.$element.on(this.handlers)};d.Defaults={autoplay:!1,autoplayTimeout:5e3,autoplayHoverPause:!1,autoplaySpeed:!1},d.prototype.autoplay=function(){this.core.settings.autoplay&&!this.core.state.videoPlay?(b.clearInterval(this.interval),this.interval=b.setInterval(a.proxy(function(){this.play()},this),this.core.settings.autoplayTimeout)):b.clearInterval(this.interval)},d.prototype.play=function(){return c.hidden===!0||this.core.state.isTouch||this.core.state.isScrolling||this.core.state.isSwiping||this.core.state.inMotion?void 0:this.core.settings.autoplay===!1?void b.clearInterval(this.interval):void this.core.next(this.core.settings.autoplaySpeed)},d.prototype.stop=function(){b.clearInterval(this.interval)},d.prototype.pause=function(){b.clearInterval(this.interval)},d.prototype.destroy=function(){var a,c;b.clearInterval(this.interval);for(a in this.handlers)this.core.$element.off(a,this.handlers[a]);for(c in Object.getOwnPropertyNames(this))"function"!=typeof this[c]&&(this[c]=null)},a.fn.owlCarousel.Constructor.Plugins.autoplay=d}(window.Zepto||window.jQuery,window,document),function(a){"use strict";var b=function(c){this._core=c,this._initialized=!1,this._pages=[],this._controls={},this._templates=[],this.$element=this._core.$element,this._overrides={next:this._core.next,prev:this._core.prev,to:this._core.to},this._handlers={"prepared.owl.carousel":a.proxy(function(b){this._core.settings.dotsData&&this._templates.push(a(b.content).find("[data-dot]").andSelf("[data-dot]").attr("data-dot"))},this),"add.owl.carousel":a.proxy(function(b){this._core.settings.dotsData&&this._templates.splice(b.position,0,a(b.content).find("[data-dot]").andSelf("[data-dot]").attr("data-dot"))},this),"remove.owl.carousel prepared.owl.carousel":a.proxy(function(a){this._core.settings.dotsData&&this._templates.splice(a.position,1)},this),"change.owl.carousel":a.proxy(function(a){if("position"==a.property.name&&!this._core.state.revert&&!this._core.settings.loop&&this._core.settings.navRewind){var b=this._core.current(),c=this._core.maximum(),d=this._core.minimum();a.data=a.property.value>c?b>=c?d:c:a.property.value<d?c:a.property.value}},this),"changed.owl.carousel":a.proxy(function(a){"position"==a.property.name&&this.draw()},this),"refreshed.owl.carousel":a.proxy(function(){this._initialized||(this.initialize(),this._initialized=!0),this._core.trigger("refresh",null,"navigation"),this.update(),this.draw(),this._core.trigger("refreshed",null,"navigation")},this)},this._core.options=a.extend({},b.Defaults,this._core.options),this.$element.on(this._handlers)};b.Defaults={nav:!1,navRewind:!0,navText:["prev","next"],navSpeed:!1,navElement:"div",navContainer:!1,navContainerClass:"owl-nav",navClass:["owl-prev","owl-next"],slideBy:1,dotClass:"owl-dot",dotsClass:"owl-dots",dots:!0,dotsEach:!1,dotData:!1,dotsSpeed:!1,dotsContainer:!1,controlsClass:"owl-controls"},b.prototype.initialize=function(){var b,c,d=this._core.settings;d.dotsData||(this._templates=[a("<div>").addClass(d.dotClass).append(a("<span>")).prop("outerHTML")]),d.navContainer&&d.dotsContainer||(this._controls.$container=a("<div>").addClass(d.controlsClass).appendTo(this.$element)),this._controls.$indicators=d.dotsContainer?a(d.dotsContainer):a("<div>").hide().addClass(d.dotsClass).appendTo(this._controls.$container),this._controls.$indicators.on("click","div",a.proxy(function(b){var c=a(b.target).parent().is(this._controls.$indicators)?a(b.target).index():a(b.target).parent().index();b.preventDefault(),this.to(c,d.dotsSpeed)},this)),b=d.navContainer?a(d.navContainer):a("<div>").addClass(d.navContainerClass).prependTo(this._controls.$container),this._controls.$next=a("<"+d.navElement+">"),this._controls.$previous=this._controls.$next.clone(),this._controls.$previous.addClass(d.navClass[0]).html(d.navText[0]).hide().prependTo(b).on("click",a.proxy(function(){this.prev(d.navSpeed)},this)),this._controls.$next.addClass(d.navClass[1]).html(d.navText[1]).hide().appendTo(b).on("click",a.proxy(function(){this.next(d.navSpeed)},this));for(c in this._overrides)this._core[c]=a.proxy(this[c],this)},b.prototype.destroy=function(){var a,b,c,d;for(a in this._handlers)this.$element.off(a,this._handlers[a]);for(b in this._controls)this._controls[b].remove();for(d in this.overides)this._core[d]=this._overrides[d];for(c in Object.getOwnPropertyNames(this))"function"!=typeof this[c]&&(this[c]=null)},b.prototype.update=function(){var a,b,c,d=this._core.settings,e=this._core.clones().length/2,f=e+this._core.items().length,g=d.center||d.autoWidth||d.dotData?1:d.dotsEach||d.items;if("page"!==d.slideBy&&(d.slideBy=Math.min(d.slideBy,d.items)),d.dots||"page"==d.slideBy)for(this._pages=[],a=e,b=0,c=0;f>a;a++)(b>=g||0===b)&&(this._pages.push({start:a-e,end:a-e+g-1}),b=0,++c),b+=this._core.mergers(this._core.relative(a))},b.prototype.draw=function(){var b,c,d="",e=this._core.settings,f=(this._core.$stage.children(),this._core.relative(this._core.current()));if(!e.nav||e.loop||e.navRewind||(this._controls.$previous.toggleClass("disabled",0>=f),this._controls.$next.toggleClass("disabled",f>=this._core.maximum())),this._controls.$previous.toggle(e.nav),this._controls.$next.toggle(e.nav),e.dots){if(b=this._pages.length-this._controls.$indicators.children().length,e.dotData&&0!==b){for(c=0;c<this._controls.$indicators.children().length;c++)d+=this._templates[this._core.relative(c)];this._controls.$indicators.html(d)}else b>0?(d=new Array(b+1).join(this._templates[0]),this._controls.$indicators.append(d)):0>b&&this._controls.$indicators.children().slice(b).remove();this._controls.$indicators.find(".active").removeClass("active"),this._controls.$indicators.children().eq(a.inArray(this.current(),this._pages)).addClass("active")}this._controls.$indicators.toggle(e.dots)},b.prototype.onTrigger=function(b){var c=this._core.settings;b.page={index:a.inArray(this.current(),this._pages),count:this._pages.length,size:c&&(c.center||c.autoWidth||c.dotData?1:c.dotsEach||c.items)}},b.prototype.current=function(){var b=this._core.relative(this._core.current());return a.grep(this._pages,function(a){return a.start<=b&&a.end>=b}).pop()},b.prototype.getPosition=function(b){var c,d,e=this._core.settings;return"page"==e.slideBy?(c=a.inArray(this.current(),this._pages),d=this._pages.length,b?++c:--c,c=this._pages[(c%d+d)%d].start):(c=this._core.relative(this._core.current()),d=this._core.items().length,b?c+=e.slideBy:c-=e.slideBy),c},b.prototype.next=function(b){a.proxy(this._overrides.to,this._core)(this.getPosition(!0),b)},b.prototype.prev=function(b){a.proxy(this._overrides.to,this._core)(this.getPosition(!1),b)},b.prototype.to=function(b,c,d){var e;d?a.proxy(this._overrides.to,this._core)(b,c):(e=this._pages.length,a.proxy(this._overrides.to,this._core)(this._pages[(b%e+e)%e].start,c))},a.fn.owlCarousel.Constructor.Plugins.Navigation=b}(window.Zepto||window.jQuery,window,document),function(a,b){"use strict";var c=function(d){this._core=d,this._hashes={},this.$element=this._core.$element,this._handlers={"initialized.owl.carousel":a.proxy(function(){"URLHash"==this._core.settings.startPosition&&a(b).trigger("hashchange.owl.navigation")},this),"prepared.owl.carousel":a.proxy(function(b){var c=a(b.content).find("[data-hash]").andSelf("[data-hash]").attr("data-hash");this._hashes[c]=b.content},this)},this._core.options=a.extend({},c.Defaults,this._core.options),this.$element.on(this._handlers),a(b).on("hashchange.owl.navigation",a.proxy(function(){var a=b.location.hash.substring(1),c=this._core.$stage.children(),d=this._hashes[a]&&c.index(this._hashes[a])||0;return a?void this._core.to(d,!1,!0):!1},this))};c.Defaults={URLhashListener:!1},c.prototype.destroy=function(){var c,d;a(b).off("hashchange.owl.navigation");for(c in this._handlers)this._core.$element.off(c,this._handlers[c]);for(d in Object.getOwnPropertyNames(this))"function"!=typeof this[d]&&(this[d]=null)},a.fn.owlCarousel.Constructor.Plugins.Hash=c}(window.Zepto||window.jQuery,window,document);
//]]>
</script>

<script>
//<![CDATA[
/*GLOBAL SETTINGS, USER CAN CHANGE*/
var FIXED_MENU = true; // to disable the fixed menu, replace "true" for "false"
var IMAGE_ANIMATE = true; // to disable the image animation, replace "true" for "false"
var MONTH_FORMAT = [, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]; // months formats to translation or change to another format
var NO_IMAGE = "http://3.bp.blogspot.com/-Yw8BIuvwoSQ/VsjkCIMoltI/AAAAAAAAC4c/s55PW6xEKn0/s1600-r/nth.png"; // default no image
var BOX_NUM = 5; // default number "no change"
var VIDEOS_NUM = 2; // default number "no change"
var CAROUSEL_NUM = 6; // show number of results carousel, default is "6"
var WIDGET_RECENT_POST_NUM = 3; // show number of results - widget recent posts
var WIDGET_RANDOM_POST_NUM = 3; // show number of results - widget random posts
var WIDGET_RECENT_COMMENT_NUM = 3; // show number of results - widget recent comments
var POSTPERPAGE_NUM = 10; // number of posts per page
var LABEL_SEARCH_NUM = 10; // number of posts labels search
var POSTNAV_PREV_TEXT = "Previous"; // post nav text "previous post"
var POSTNAV_NEXT_TEXT = "Next"; // post nav text "next post"

/*JQUERY PLUGINS*/

// JQuery hover event with timeout by Taufik Nurrohman - https://plus.google.com/108949996304093815163/about
(function(c){c.fn.hoverTimeout=function(d,e,f,g){return this.each(function(){var a=null,b=c(this);b.hover(function(){clearTimeout(a);a=setTimeout(function(){e.call(b)},d)},function(){clearTimeout(a);a=setTimeout(function(){g.call(b)},f)})})}})(jQuery);

// jquery replacetext plugin https://github.com/cowboy/jquery-replacetext
(function(e){e.fn.replaceText=function(t,n,r){return this.each(function(){var i=this.firstChild,s,o,u=[];if(i){do{if(i.nodeType===3){s=i.nodeValue;o=s.replace(t,n);if(o!==s){if(!r&&/</.test(o)){e(i).before(o);u.push(i)}else{i.nodeValue=o}}}}while(i=i.nextSibling)}u.length&&e(u).remove()})}})(jQuery);

// Plugin: SelectNav.js ~ url: https://github.com/lukaszfiszer/selectnav.js
window.selectnav=function(){"use strict";var e=function(e,t){function c(e){var t;if(!e)e=window.event;if(e.target)t=e.target;else if(e.srcElement)t=e.srcElement;if(t.nodeType===3)t=t.parentNode;if(t.value)window.location.href=t.value}function h(e){var t=e.nodeName.toLowerCase();return t==="ul"||t==="ol"}function p(e){for(var t=1;document.getElementById("selectnav"+t);t++);return e?"selectnav"+t:"selectnav"+(t-1)}function d(e){a++;var t=e.children.length,n="",l="",c=a-1;if(!t){return}if(c){while(c--){l+=o}l+=" "}for(var v=0;v<t;v++){var m=e.children[v].children[0];if(typeof m!=="undefined"){var g=m.innerText||m.textContent;var y="";if(r){y=m.className.search(r)!==-1||m.parentNode.className.search(r)!==-1?f:""}if(i&&!y){y=m.href===document.URL?f:""}n+='<option value="'+m.href+'" '+y+">"+l+g+"</option>";if(s){var b=e.children[v].children[1];if(b&&h(b)){n+=d(b)}}}}if(a===1&&u){n='<option value="">'+u+"</option>"+n}if(a===1){n='<select class="selectnav" id="'+p(true)+'">'+n+"</select>"}a--;return n}e=document.getElementById(e);if(!e){return}if(!h(e)){return}if(!("insertAdjacentHTML"in window.document.documentElement)){return}document.documentElement.className+=" js";var n=t||{},r=n.activeclass||"active",i=typeof n.autoselect==="boolean"?n.autoselect:true,s=typeof n.nested==="boolean"?n.nested:true,o=n.indent||"→",u=n.label||"Menu",a=0,f=" selected ";e.insertAdjacentHTML("afterend",d(e));var l=document.getElementById(p());if(l.addEventListener){l.addEventListener("change",c)}if(l.attachEvent){l.attachEvent("onchange",c)}return l};return function(t,n){e(t,n)}}();$(document).ready(function(){selectnav('menu-main-nav');selectnav('nav1');});

// Main Scripts
var _0x9a81=["\x31\x53\x20\x31\x36\x3D\x5B\x22\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x38\x5C\x65\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x50\x5C\x73\x5C\x65\x5C\x4E\x5C\x54\x5C\x6A\x5C\x69\x5C\x31\x72\x5C\x73\x5C\x6E\x5C\x31\x32\x5C\x74\x5C\x31\x6C\x5C\x74\x5C\x31\x39\x5C\x6E\x5C\x4D\x5C\x4E\x5C\x42\x5C\x4D\x5C\x4E\x5C\x54\x5C\x6A\x5C\x5A\x5C\x73\x5C\x6E\x5C\x66\x5C\x58\x5C\x74\x5C\x31\x32\x5C\x6E\x5C\x4D\x5C\x65\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x38\x5C\x6A\x5C\x42\x5C\x65\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x67\x5C\x73\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x31\x43\x5C\x61\x5C\x62\x5C\x6F\x5C\x6D\x5C\x73\x5C\x67\x5C\x64\x5C\x66\x5C\x72\x5C\x61\x5C\x58\x5C\x6F\x5C\x66\x5C\x62\x5C\x6F\x5C\x4A\x5C\x73\x5C\x67\x5C\x64\x5C\x66\x5C\x72\x5C\x61\x5C\x66\x5C\x62\x5C\x7A\x5C\x65\x5C\x69\x5C\x77\x5C\x65\x5C\x73\x5C\x73\x5C\x6D\x5C\x31\x46\x5C\x61\x5C\x6D\x5C\x73\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x4F\x5C\x61\x5C\x65\x5C\x67\x5C\x65\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x65\x5C\x31\x30\x5C\x65\x5C\x62\x5C\x6F\x5C\x50\x5C\x4C\x5C\x73\x5C\x6E\x5C\x4E\x5C\x42\x5C\x4D\x5C\x4E\x5C\x67\x5C\x6A\x5C\x31\x30\x5C\x73\x5C\x65\x5C\x6E\x5C\x4C\x5C\x6D\x5C\x4C\x5C\x6E\x5C\x65\x5C\x4D\x5C\x6E\x5C\x4C\x5C\x4A\x5C\x4C\x5C\x65\x5C\x4E\x5C\x71\x5C\x67\x5C\x4D\x5C\x4E\x5C\x71\x5C\x42\x5C\x4D\x5C\x65\x5C\x62\x5C\x31\x75\x5C\x61\x5C\x6D\x5C\x73\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x4F\x5C\x61\x5C\x65\x5C\x67\x5C\x65\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x65\x5C\x31\x30\x5C\x65\x5C\x62\x5C\x6F\x5C\x50\x5C\x4C\x5C\x73\x5C\x6E\x5C\x4E\x5C\x71\x5C\x54\x5C\x4D\x5C\x4E\x5C\x71\x5C\x42\x5C\x4D\x5C\x4E\x5C\x42\x5C\x4D\x5C\x4E\x5C\x67\x5C\x6A\x5C\x31\x30\x5C\x73\x5C\x65\x5C\x6E\x5C\x4C\x5C\x6D\x5C\x4C\x5C\x6E\x5C\x65\x5C\x4D\x5C\x6E\x5C\x4C\x5C\x67\x5C\x4C\x5C\x65\x5C\x4E\x5C\x71\x5C\x67\x5C\x4D\x5C\x4E\x5C\x54\x5C\x6A\x5C\x5A\x5C\x73\x5C\x6E\x5C\x66\x5C\x58\x5C\x74\x5C\x31\x32\x5C\x6E\x5C\x4D\x5C\x65\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x50\x5C\x4C\x5C\x73\x5C\x65\x5C\x4E\x5C\x71\x5C\x54\x5C\x4D\x5C\x4E\x5C\x71\x5C\x42\x5C\x4D\x5C\x4E\x5C\x71\x5C\x54\x5C\x4D\x5C\x65\x5C\x7A\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x72\x5C\x61\x5C\x50\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x38\x5C\x6A\x5C\x54\x5C\x65\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x50\x5C\x73\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x7A\x5C\x31\x37\x5C\x61\x5C\x50\x5C\x64\x5C\x72\x5C\x61\x5C\x62\x5C\x64\x5C\x48\x5C\x61\x5C\x71\x5C\x31\x73\x5C\x70\x5C\x63\x5C\x31\x79\x5C\x66\x5C\x67\x5C\x7A\x5C\x71\x5C\x4B\x5C\x6F\x5C\x65\x5C\x65\x5C\x62\x5C\x64\x5C\x49\x5C\x73\x5C\x73\x5C\x58\x5C\x62\x5C\x50\x5C\x64\x5C\x66\x5C\x51\x5C\x61\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x38\x5C\x6A\x5C\x42\x5C\x65\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x50\x5C\x73\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x7A\x5C\x31\x37\x5C\x61\x5C\x50\x5C\x64\x5C\x72\x5C\x61\x5C\x62\x5C\x64\x5C\x48\x5C\x61\x5C\x71\x5C\x31\x73\x5C\x70\x5C\x63\x5C\x31\x79\x5C\x66\x5C\x67\x5C\x7A\x5C\x71\x5C\x4B\x5C\x6F\x5C\x65\x5C\x65\x5C\x62\x5C\x64\x5C\x49\x5C\x73\x5C\x73\x5C\x58\x5C\x62\x5C\x50\x5C\x64\x5C\x66\x5C\x51\x5C\x61\x5C\x62\x5C\x45\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x31\x33\x5C\x62\x5C\x64\x5C\x31\x6F\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x32\x5C\x65\x5C\x62\x5C\x64\x5C\x69\x5C\x47\x5C\x61\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x54\x5C\x64\x5C\x66\x5C\x58\x5C\x74\x5C\x31\x32\x5C\x65\x5C\x62\x5C\x64\x5C\x69\x5C\x66\x5C\x61\x5C\x65\x5C\x42\x5C\x65\x5C\x62\x5C\x64\x5C\x31\x76\x5C\x61\x5C\x65\x5C\x69\x5C\x67\x5C\x74\x5C\x59\x5C\x65\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x32\x5C\x6A\x5C\x54\x5C\x6A\x5C\x42\x5C\x65\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x66\x5C\x31\x69\x5C\x61\x5C\x58\x5C\x6F\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x59\x5C\x61\x5C\x65\x5C\x54\x5C\x65\x5C\x62\x5C\x64\x5C\x69\x5C\x31\x6B\x5C\x61\x5C\x62\x5C\x45\x5C\x6F\x5C\x58\x5C\x6F\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x59\x5C\x61\x5C\x65\x5C\x54\x5C\x65\x5C\x62\x5C\x64\x5C\x69\x5C\x50\x5C\x61\x5C\x62\x5C\x45\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x66\x5C\x48\x5C\x74\x5C\x66\x5C\x31\x71\x5C\x65\x5C\x62\x5C\x64\x5C\x69\x5C\x76\x5C\x61\x5C\x65\x5C\x66\x5C\x42\x5C\x65\x5C\x6F\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x39\x5C\x74\x5C\x66\x5C\x48\x5C\x65\x5C\x62\x5C\x64\x5C\x66\x5C\x31\x74\x5C\x61\x5C\x66\x5C\x31\x78\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x53\x5C\x6A\x5C\x41\x5C\x73\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x6C\x5C\x74\x5C\x31\x39\x5C\x6A\x5C\x31\x35\x5C\x70\x5C\x65\x5C\x62\x5C\x64\x5C\x69\x5C\x43\x5C\x61\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x6C\x5C\x74\x5C\x31\x39\x5C\x6A\x5C\x31\x35\x5C\x70\x5C\x65\x5C\x62\x5C\x64\x5C\x69\x5C\x4B\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x31\x37\x5C\x61\x5C\x58\x5C\x73\x5C\x73\x5C\x73\x5C\x47\x5C\x64\x5C\x31\x62\x5C\x64\x5C\x49\x5C\x62\x5C\x47\x5C\x64\x5C\x31\x62\x5C\x73\x5C\x41\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x35\x5C\x31\x6C\x5C\x74\x5C\x31\x39\x5C\x6A\x5C\x31\x35\x5C\x70\x5C\x65\x5C\x62\x5C\x64\x5C\x69\x5C\x31\x64\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x31\x37\x5C\x61\x5C\x47\x5C\x64\x5C\x31\x62\x5C\x73\x5C\x73\x5C\x73\x5C\x41\x5C\x62\x5C\x47\x5C\x64\x5C\x31\x62\x5C\x73\x5C\x65\x5C\x65\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x64\x5C\x66\x5C\x47\x5C\x6A\x5C\x64\x5C\x6C\x5C\x74\x5C\x31\x64\x5C\x6F\x5C\x64\x5C\x66\x5C\x66\x5C\x6A\x5C\x64\x5C\x6C\x5C\x74\x5C\x31\x64\x5C\x65\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x4F\x5C\x61\x5C\x65\x5C\x64\x5C\x31\x63\x5C\x74\x5C\x31\x34\x5C\x6A\x5C\x64\x5C\x52\x5C\x6A\x5C\x67\x5C\x65\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x65\x5C\x31\x67\x5C\x65\x5C\x6F\x5C\x69\x5C\x61\x5C\x67\x5C\x6F\x5C\x43\x5C\x62\x5C\x46\x5C\x6B\x5C\x6A\x5C\x43\x5C\x64\x5C\x48\x5C\x61\x5C\x65\x5C\x71\x5C\x66\x5C\x4B\x5C\x64\x5C\x31\x31\x5C\x65\x5C\x6F\x5C\x65\x5C\x71\x5C\x66\x5C\x4F\x5C\x64\x5C\x31\x31\x5C\x65\x5C\x62\x5C\x45\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x65\x5C\x31\x67\x5C\x65\x5C\x6F\x5C\x69\x5C\x61\x5C\x67\x5C\x6F\x5C\x43\x5C\x62\x5C\x46\x5C\x6B\x5C\x6A\x5C\x43\x5C\x64\x5C\x48\x5C\x61\x5C\x65\x5C\x66\x5C\x31\x32\x5C\x74\x5C\x41\x5C\x65\x5C\x6F\x5C\x65\x5C\x31\x74\x5C\x65\x5C\x62\x5C\x45\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x64\x5C\x66\x5C\x47\x5C\x6A\x5C\x64\x5C\x6C\x5C\x74\x5C\x31\x64\x5C\x6F\x5C\x64\x5C\x66\x5C\x66\x5C\x6A\x5C\x64\x5C\x6C\x5C\x74\x5C\x31\x64\x5C\x65\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x4F\x5C\x61\x5C\x65\x5C\x64\x5C\x31\x63\x5C\x74\x5C\x31\x34\x5C\x6A\x5C\x64\x5C\x52\x5C\x6A\x5C\x67\x5C\x65\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x65\x5C\x31\x67\x5C\x65\x5C\x6F\x5C\x69\x5C\x61\x5C\x67\x5C\x6F\x5C\x43\x5C\x62\x5C\x46\x5C\x6B\x5C\x6A\x5C\x43\x5C\x64\x5C\x48\x5C\x61\x5C\x65\x5C\x31\x78\x5C\x31\x75\x5C\x71\x5C\x71\x5C\x31\x6A\x5C\x64\x5C\x66\x5C\x31\x6A\x5C\x64\x5C\x66\x5C\x31\x77\x5C\x64\x5C\x31\x65\x5C\x71\x5C\x74\x5C\x66\x5C\x31\x62\x5C\x71\x5C\x66\x5C\x31\x70\x5C\x71\x5C\x66\x5C\x31\x67\x5C\x71\x5C\x66\x5C\x59\x5C\x71\x5C\x31\x74\x5C\x74\x5C\x77\x5C\x71\x5C\x66\x5C\x31\x63\x5C\x64\x5C\x66\x5C\x53\x5C\x65\x5C\x6F\x5C\x65\x5C\x65\x5C\x4C\x5C\x69\x5C\x58\x5C\x4C\x5C\x65\x5C\x65\x5C\x62\x5C\x45\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x6E\x5C\x64\x5C\x31\x72\x5C\x6A\x5C\x54\x5C\x6A\x5C\x42\x5C\x6A\x5C\x44\x5C\x6E\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x6E\x5C\x55\x5C\x6E\x5C\x6F\x5C\x69\x5C\x61\x5C\x76\x5C\x6F\x5C\x55\x5C\x62\x5C\x46\x5C\x6B\x5C\x6A\x5C\x55\x5C\x64\x5C\x48\x5C\x61\x5C\x6E\x5C\x71\x5C\x66\x5C\x4B\x5C\x64\x5C\x31\x31\x5C\x6E\x5C\x6F\x5C\x6E\x5C\x71\x5C\x66\x5C\x4F\x5C\x64\x5C\x31\x31\x5C\x6E\x5C\x62\x5C\x45\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x6E\x5C\x55\x5C\x6E\x5C\x6F\x5C\x69\x5C\x61\x5C\x76\x5C\x6F\x5C\x55\x5C\x62\x5C\x46\x5C\x6B\x5C\x6A\x5C\x55\x5C\x64\x5C\x48\x5C\x61\x5C\x6E\x5C\x66\x5C\x31\x32\x5C\x74\x5C\x41\x5C\x6E\x5C\x6F\x5C\x6E\x5C\x31\x74\x5C\x6E\x5C\x62\x5C\x45\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x64\x5C\x31\x72\x5C\x6A\x5C\x64\x5C\x66\x5C\x54\x5C\x74\x5C\x66\x5C\x55\x5C\x6A\x5C\x67\x5C\x65\x5C\x62\x5C\x64\x5C\x69\x5C\x31\x30\x5C\x61\x5C\x6E\x5C\x4E\x5C\x57\x5C\x6A\x5C\x5A\x5C\x73\x5C\x65\x5C\x44\x5C\x74\x5C\x69\x5C\x72\x5C\x65\x5C\x71\x5C\x4D\x5C\x6E\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x64\x5C\x69\x5C\x4A\x5C\x6A\x5C\x64\x5C\x66\x5C\x43\x5C\x6A\x5C\x31\x6E\x5C\x6F\x5C\x64\x5C\x69\x5C\x31\x65\x5C\x74\x5C\x69\x5C\x31\x39\x5C\x6A\x5C\x64\x5C\x66\x5C\x43\x5C\x6A\x5C\x31\x6E\x5C\x65\x5C\x62\x5C\x64\x5C\x66\x5C\x41\x5C\x61\x5C\x65\x5C\x4E\x5C\x69\x5C\x5A\x5C\x6A\x5C\x5A\x5C\x73\x5C\x6E\x5C\x79\x5C\x74\x5C\x66\x5C\x41\x5C\x6E\x5C\x71\x5C\x4D\x5C\x65\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x6E\x5C\x64\x5C\x66\x5C\x69\x5C\x74\x5C\x31\x34\x5C\x74\x5C\x66\x5C\x57\x5C\x6A\x5C\x44\x5C\x6E\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x6E\x5C\x55\x5C\x6E\x5C\x6F\x5C\x69\x5C\x61\x5C\x76\x5C\x6F\x5C\x55\x5C\x62\x5C\x46\x5C\x6B\x5C\x6A\x5C\x55\x5C\x64\x5C\x48\x5C\x61\x5C\x6E\x5C\x71\x5C\x71\x5C\x66\x5C\x31\x6F\x5C\x64\x5C\x66\x5C\x31\x72\x5C\x64\x5C\x31\x65\x5C\x71\x5C\x44\x5C\x71\x5C\x66\x5C\x31\x6C\x5C\x64\x5C\x66\x5C\x31\x31\x5C\x6E\x5C\x6F\x5C\x6E\x5C\x71\x5C\x71\x5C\x31\x77\x5C\x64\x5C\x66\x5C\x31\x6A\x5C\x64\x5C\x66\x5C\x31\x77\x5C\x64\x5C\x31\x65\x5C\x71\x5C\x74\x5C\x66\x5C\x31\x6E\x5C\x71\x5C\x66\x5C\x31\x6B\x5C\x74\x5C\x66\x5C\x5A\x5C\x71\x5C\x66\x5C\x31\x64\x5C\x71\x5C\x66\x5C\x31\x61\x5C\x71\x5C\x66\x5C\x68\x5C\x74\x5C\x77\x5C\x71\x5C\x66\x5C\x69\x5C\x64\x5C\x66\x5C\x53\x5C\x6E\x5C\x62\x5C\x45\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x6E\x5C\x55\x5C\x6E\x5C\x6F\x5C\x69\x5C\x61\x5C\x76\x5C\x6F\x5C\x55\x5C\x62\x5C\x46\x5C\x6B\x5C\x6A\x5C\x55\x5C\x64\x5C\x48\x5C\x61\x5C\x6E\x5C\x71\x5C\x66\x5C\x31\x38\x5C\x6E\x5C\x6F\x5C\x6E\x5C\x71\x5C\x66\x5C\x68\x5C\x6E\x5C\x62\x5C\x45\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x65\x5C\x64\x5C\x66\x5C\x31\x34\x5C\x74\x5C\x31\x6D\x5C\x65\x5C\x62\x5C\x64\x5C\x66\x5C\x42\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x31\x37\x5C\x61\x5C\x31\x71\x5C\x64\x5C\x66\x5C\x78\x5C\x64\x5C\x48\x5C\x61\x5C\x71\x5C\x31\x48\x5C\x31\x73\x5C\x71\x5C\x71\x5C\x6F\x5C\x65\x5C\x65\x5C\x62\x5C\x73\x5C\x73\x5C\x47\x5C\x64\x5C\x66\x5C\x78\x5C\x64\x5C\x48\x5C\x61\x5C\x71\x5C\x31\x48\x5C\x31\x73\x5C\x71\x5C\x71\x5C\x6F\x5C\x65\x5C\x65\x5C\x62\x5C\x31\x79\x5C\x31\x79\x5C\x31\x71\x5C\x64\x5C\x66\x5C\x76\x5C\x73\x5C\x73\x5C\x47\x5C\x64\x5C\x66\x5C\x76\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x67\x5C\x73\x5C\x75\x5C\x61\x5C\x47\x5C\x64\x5C\x66\x5C\x31\x30\x5C\x62\x5C\x7A\x5C\x67\x5C\x73\x5C\x67\x5C\x64\x5C\x49\x5C\x31\x46\x5C\x67\x5C\x31\x75\x5C\x75\x5C\x61\x5C\x65\x5C\x31\x50\x5C\x66\x5C\x31\x76\x5C\x73\x5C\x65\x5C\x4C\x5C\x47\x5C\x64\x5C\x66\x5C\x31\x30\x5C\x64\x5C\x66\x5C\x31\x6D\x5C\x61\x5C\x66\x5C\x62\x5C\x4C\x5C\x65\x5C\x31\x51\x5C\x65\x5C\x62\x5C\x7A\x5C\x31\x37\x5C\x61\x5C\x67\x5C\x64\x5C\x49\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x65\x5C\x72\x5C\x6F\x5C\x66\x5C\x50\x5C\x65\x5C\x62\x5C\x64\x5C\x66\x5C\x31\x43\x5C\x61\x5C\x46\x5C\x66\x5C\x6C\x5C\x31\x75\x5C\x67\x5C\x64\x5C\x66\x5C\x79\x5C\x61\x5C\x62\x5C\x64\x5C\x31\x6D\x5C\x45\x5C\x6F\x5C\x69\x5C\x69\x5C\x62\x5C\x7A\x5C\x6B\x5C\x6A\x5C\x69\x5C\x31\x6A\x5C\x45\x5C\x45\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x31\x33\x5C\x62\x5C\x64\x5C\x31\x6F\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x6E\x5C\x66\x5C\x50\x5C\x6E\x5C\x62\x5C\x64\x5C\x31\x76\x5C\x61\x5C\x6E\x5C\x44\x5C\x74\x5C\x69\x5C\x31\x77\x5C\x6E\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x31\x69\x5C\x62\x5C\x64\x5C\x69\x5C\x53\x5C\x61\x5C\x6E\x5C\x69\x5C\x51\x5C\x6A\x5C\x69\x5C\x54\x5C\x6A\x5C\x69\x5C\x55\x5C\x6E\x5C\x6F\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x31\x69\x5C\x73\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x66\x5C\x6D\x5C\x61\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x6E\x5C\x64\x5C\x66\x5C\x4A\x5C\x74\x5C\x31\x34\x5C\x6F\x5C\x64\x5C\x69\x5C\x41\x5C\x74\x5C\x52\x5C\x6F\x5C\x64\x5C\x69\x5C\x42\x5C\x6F\x5C\x64\x5C\x31\x72\x5C\x6A\x5C\x44\x5C\x6F\x5C\x64\x5C\x69\x5C\x68\x5C\x6A\x5C\x64\x5C\x31\x63\x5C\x74\x5C\x31\x34\x5C\x6A\x5C\x64\x5C\x52\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x69\x5C\x48\x5C\x74\x5C\x52\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x66\x5C\x31\x37\x5C\x74\x5C\x52\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x31\x72\x5C\x6A\x5C\x64\x5C\x66\x5C\x54\x5C\x74\x5C\x66\x5C\x55\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x69\x5C\x78\x5C\x74\x5C\x44\x5C\x6E\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x66\x5C\x77\x5C\x73\x5C\x64\x5C\x66\x5C\x31\x52\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x66\x5C\x6D\x5C\x61\x5C\x62\x5C\x7A\x5C\x53\x5C\x6A\x5C\x66\x5C\x70\x5C\x73\x5C\x66\x5C\x77\x5C\x74\x5C\x31\x69\x5C\x4C\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x66\x5C\x79\x5C\x61\x5C\x62\x5C\x64\x5C\x31\x6D\x5C\x7A\x5C\x53\x5C\x6A\x5C\x66\x5C\x6B\x5C\x73\x5C\x75\x5C\x61\x5C\x31\x33\x5C\x62\x5C\x64\x5C\x66\x5C\x6C\x5C\x61\x5C\x62\x5C\x7A\x5C\x31\x37\x5C\x61\x5C\x66\x5C\x6B\x5C\x4D\x5C\x66\x5C\x70\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x31\x76\x5C\x61\x5C\x6E\x5C\x44\x5C\x74\x5C\x69\x5C\x6C\x5C\x6E\x5C\x62\x5C\x45\x5C\x45\x5C\x62\x5C\x45\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x31\x33\x5C\x62\x5C\x64\x5C\x31\x6F\x5C\x61\x5C\x69\x5C\x61\x5C\x67\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x43\x5C\x73\x5C\x67\x5C\x61\x5C\x65\x5C\x67\x5C\x64\x5C\x69\x5C\x79\x5C\x74\x5C\x66\x5C\x44\x5C\x65\x5C\x62\x5C\x7A\x5C\x53\x5C\x6A\x5C\x41\x5C\x73\x5C\x67\x5C\x61\x5C\x65\x5C\x67\x5C\x64\x5C\x69\x5C\x6D\x5C\x74\x5C\x66\x5C\x44\x5C\x65\x5C\x62\x5C\x7A\x5C\x67\x5C\x64\x5C\x66\x5C\x52\x5C\x61\x5C\x43\x5C\x64\x5C\x51\x5C\x61\x5C\x65\x5C\x31\x30\x5C\x65\x5C\x62\x5C\x6F\x5C\x69\x5C\x61\x5C\x41\x5C\x62\x5C\x46\x5C\x43\x5C\x64\x5C\x72\x5C\x61\x5C\x65\x5C\x4E\x5C\x31\x6B\x5C\x4D\x5C\x65\x5C\x4C\x5C\x69\x5C\x31\x37\x5C\x4C\x5C\x65\x5C\x4E\x5C\x71\x5C\x31\x6B\x5C\x4D\x5C\x4E\x5C\x57\x5C\x4D\x5C\x65\x5C\x4C\x5C\x67\x5C\x61\x5C\x41\x5C\x62\x5C\x64\x5C\x4F\x5C\x61\x5C\x65\x5C\x64\x5C\x6C\x5C\x6A\x5C\x66\x5C\x31\x33\x5C\x64\x5C\x6C\x5C\x74\x5C\x79\x5C\x65\x5C\x62\x5C\x64\x5C\x31\x43\x5C\x61\x5C\x62\x5C\x4C\x5C\x65\x5C\x4E\x5C\x71\x5C\x57\x5C\x4D\x5C\x65\x5C\x62\x5C\x45\x5C\x6F\x5C\x65\x5C\x72\x5C\x65\x5C\x62\x5C\x7A\x5C\x67\x5C\x64\x5C\x66\x5C\x52\x5C\x61\x5C\x41\x5C\x64\x5C\x51\x5C\x61\x5C\x65\x5C\x31\x30\x5C\x65\x5C\x62\x5C\x6F\x5C\x69\x5C\x61\x5C\x43\x5C\x62\x5C\x46\x5C\x41\x5C\x64\x5C\x72\x5C\x61\x5C\x65\x5C\x4E\x5C\x31\x6B\x5C\x4D\x5C\x65\x5C\x4C\x5C\x69\x5C\x70\x5C\x4C\x5C\x65\x5C\x4E\x5C\x71\x5C\x31\x6B\x5C\x4D\x5C\x4E\x5C\x57\x5C\x4D\x5C\x65\x5C\x4C\x5C\x67\x5C\x61\x5C\x43\x5C\x62\x5C\x64\x5C\x4F\x5C\x61\x5C\x65\x5C\x64\x5C\x6C\x5C\x6A\x5C\x66\x5C\x31\x33\x5C\x64\x5C\x6C\x5C\x74\x5C\x79\x5C\x65\x5C\x62\x5C\x64\x5C\x31\x43\x5C\x61\x5C\x62\x5C\x4C\x5C\x65\x5C\x4E\x5C\x71\x5C\x57\x5C\x4D\x5C\x65\x5C\x62\x5C\x45\x5C\x6F\x5C\x65\x5C\x72\x5C\x65\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x31\x33\x5C\x62\x5C\x64\x5C\x31\x6F\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x75\x5C\x61\x5C\x6E\x5C\x64\x5C\x69\x5C\x6B\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x69\x5C\x44\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x69\x5C\x52\x5C\x74\x5C\x69\x5C\x4F\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x66\x5C\x4A\x5C\x74\x5C\x79\x5C\x6A\x5C\x31\x6E\x5C\x64\x5C\x79\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x69\x5C\x31\x33\x5C\x74\x5C\x79\x5C\x6A\x5C\x31\x6E\x5C\x64\x5C\x79\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x69\x5C\x31\x32\x5C\x74\x5C\x31\x61\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x69\x5C\x49\x5C\x74\x5C\x31\x61\x5C\x6A\x5C\x67\x5C\x6F\x5C\x64\x5C\x6C\x5C\x74\x5C\x31\x61\x5C\x6F\x5C\x64\x5C\x66\x5C\x31\x37\x5C\x74\x5C\x31\x61\x5C\x6E\x5C\x62\x5C\x64\x5C\x78\x5C\x61\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x66\x5C\x31\x65\x5C\x73\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x6E\x5C\x31\x30\x5C\x6E\x5C\x62\x5C\x7A\x5C\x75\x5C\x61\x5C\x47\x5C\x62\x5C\x64\x5C\x51\x5C\x61\x5C\x6E\x5C\x31\x30\x5C\x6E\x5C\x6F\x5C\x66\x5C\x31\x65\x5C\x4C\x5C\x6E\x5C\x31\x46\x5C\x31\x79\x5C\x69\x5C\x31\x34\x5C\x74\x5C\x69\x5C\x31\x69\x5C\x73\x5C\x6E\x5C\x4C\x5C\x69\x5C\x57\x5C\x4C\x5C\x6E\x5C\x6E\x5C\x62\x5C\x45\x5C\x62\x5C\x45\x5C\x62\x5C\x7A\x5C\x31\x69\x5C\x64\x5C\x69\x5C\x31\x6F\x5C\x73\x5C\x69\x5C\x61\x5C\x62\x5C\x46\x5C\x53\x5C\x6A\x5C\x68\x5C\x73\x5C\x31\x33\x5C\x64\x5C\x69\x5C\x31\x6C\x5C\x61\x5C\x65\x5C\x69\x5C\x31\x31\x5C\x65\x5C\x62\x5C\x7A\x5C\x31\x37\x5C\x61\x5C\x68\x5C\x73\x5C\x73\x5C\x69\x5C\x31\x6E\x5C\x62\x5C\x46\x5C\x31\x69\x5C\x64\x5C\x31\x71\x5C\x64\x5C\x31\x30\x5C\x73\x5C\x65\x5C\x31\x78\x5C\x31\x75\x5C\x71\x5C\x71\x5C\x66\x5C\x49\x5C\x64\x5C\x66\x5C\x31\x39\x5C\x64\x5C\x31\x65\x5C\x71\x5C\x65\x5C\x45\x5C\x68\x5C\x64\x5C\x31\x70\x5C\x61\x5C\x65\x5C\x31\x30\x5C\x65\x5C\x6F\x5C\x65\x5C\x31\x78\x5C\x31\x75\x5C\x71\x5C\x71\x5C\x66\x5C\x49\x5C\x64\x5C\x66\x5C\x31\x39\x5C\x64\x5C\x31\x65\x5C\x71\x5C\x65\x5C\x62\x5C\x7A\x5C\x68\x5C\x64\x5C\x31\x70\x5C\x61\x5C\x65\x5C\x69\x5C\x31\x61\x5C\x65\x5C\x6F\x5C\x65\x5C\x69\x5C\x31\x62\x5C\x65\x5C\x62\x5C\x7A\x5C\x68\x5C\x64\x5C\x31\x70\x5C\x61\x5C\x65\x5C\x79\x5C\x65\x5C\x6F\x5C\x65\x5C\x69\x5C\x31\x38\x5C\x6A\x5C\x69\x5C\x31\x78\x5C\x65\x5C\x62\x5C\x7A\x5C\x68\x5C\x64\x5C\x69\x5C\x31\x70\x5C\x73\x5C\x65\x5C\x69\x5C\x31\x67\x5C\x65\x5C\x45\x22\x2C\x22\x5C\x63\x22\x2C\x22\x5C\x70\x5C\x4A\x5C\x6C\x5C\x76\x5C\x6B\x22\x2C\x22\x5C\x63\x5C\x63\x5C\x48\x5C\x44\x5C\x72\x5C\x41\x5C\x6B\x5C\x76\x5C\x6D\x5C\x72\x5C\x63\x5C\x63\x5C\x63\x5C\x6B\x5C\x78\x5C\x76\x5C\x70\x5C\x63\x5C\x52\x5C\x67\x5C\x77\x5C\x63\x5C\x67\x5C\x6B\x5C\x6B\x5C\x77\x5C\x63\x5C\x44\x5C\x6C\x5C\x63\x5C\x70\x5C\x77\x5C\x41\x5C\x63\x5C\x63\x5C\x63\x5C\x63\x5C\x6C\x5C\x76\x5C\x63\x5C\x63\x5C\x77\x5C\x68\x5C\x4A\x5C\x6C\x5C\x67\x5C\x41\x5C\x68\x5C\x63\x5C\x63\x5C\x68\x5C\x67\x5C\x41\x5C\x78\x5C\x63\x5C\x63\x5C\x78\x5C\x77\x5C\x68\x5C\x48\x5C\x63\x5C\x63\x5C\x4A\x5C\x6D\x5C\x70\x5C\x6B\x5C\x63\x5C\x6B\x5C\x76\x5C\x6B\x5C\x6C\x5C\x68\x5C\x63\x5C\x78\x5C\x6B\x5C\x79\x5C\x6C\x5C\x63\x5C\x63\x5C\x63\x5C\x76\x5C\x48\x5C\x63\x5C\x63\x5C\x63\x5C\x77\x5C\x68\x5C\x6B\x5C\x44\x5C\x77\x5C\x72\x5C\x63\x5C\x76\x5C\x79\x5C\x4B\x5C\x63\x5C\x6B\x5C\x78\x5C\x44\x5C\x79\x5C\x43\x5C\x63\x5C\x48\x5C\x76\x5C\x72\x5C\x42\x5C\x63\x5C\x42\x5C\x6D\x5C\x41\x5C\x44\x5C\x79\x5C\x68\x5C\x72\x5C\x6B\x5C\x63\x5C\x79\x5C\x68\x5C\x72\x5C\x44\x5C\x63\x5C\x41\x5C\x6D\x5C\x79\x5C\x63\x5C\x6C\x5C\x68\x5C\x72\x5C\x4B\x5C\x6B\x5C\x78\x5C\x63\x5C\x72\x5C\x67\x5C\x52\x5C\x63\x5C\x76\x5C\x79\x5C\x67\x5C\x4B\x5C\x68\x5C\x63\x5C\x4F\x5C\x76\x5C\x72\x5C\x42\x5C\x6D\x5C\x4F\x5C\x63\x5C\x70\x5C\x4A\x5C\x67\x5C\x72\x5C\x63\x5C\x77\x5C\x68\x5C\x67\x5C\x42\x5C\x31\x32\x5C\x63\x5C\x31\x38\x5C\x6D\x5C\x4A\x5C\x44\x5C\x6C\x5C\x67\x5C\x77\x5C\x31\x38\x5C\x6D\x5C\x70\x5C\x6B\x5C\x70\x5C\x63\x5C\x79\x5C\x67\x5C\x76\x5C\x72\x5C\x63\x5C\x31\x30\x5C\x4A\x5C\x4B\x5C\x63\x5C\x78\x5C\x69\x5C\x63\x5C\x70\x5C\x6B\x5C\x77\x5C\x6D\x5C\x72\x5C\x4B\x5C\x63\x5C\x41\x5C\x6C\x5C\x67\x5C\x70\x5C\x70\x5C\x63\x5C\x6D\x5C\x44\x5C\x6B\x5C\x68\x5C\x77\x5C\x63\x5C\x6B\x5C\x67\x5C\x4B\x5C\x63\x5C\x52\x5C\x67\x5C\x6C\x5C\x44\x5C\x68\x5C\x63\x5C\x5A\x5C\x76\x5C\x72\x5C\x50\x5C\x5A\x5C\x76\x5C\x70\x5C\x6B\x5C\x55\x5C\x54\x5C\x63\x5C\x78\x5C\x6B\x5C\x6B\x5C\x4A\x5C\x63\x5C\x70\x5C\x68\x5C\x6B\x5C\x49\x5C\x6B\x5C\x6B\x5C\x77\x5C\x76\x5C\x43\x5C\x44\x5C\x6B\x5C\x68\x5C\x63\x5C\x70\x5C\x6B\x5C\x31\x32\x5C\x6C\x5C\x68\x5C\x63\x5C\x41\x5C\x78\x5C\x76\x5C\x6C\x5C\x42\x5C\x77\x5C\x68\x5C\x72\x5C\x63\x5C\x70\x5C\x66\x5C\x53\x5C\x58\x5C\x58\x5C\x63\x5C\x43\x5C\x6C\x5C\x6D\x5C\x41\x5C\x50\x5C\x63\x5C\x67\x5C\x42\x5C\x42\x5C\x31\x34\x5C\x6C\x5C\x67\x5C\x70\x5C\x70\x5C\x63\x5C\x6B\x5C\x6D\x5C\x4A\x5C\x63\x5C\x6C\x5C\x6D\x5C\x41\x5C\x67\x5C\x6B\x5C\x76\x5C\x6D\x5C\x72\x5C\x63\x5C\x6B\x5C\x68\x5C\x31\x33\x5C\x6B\x5C\x63\x5C\x70\x5C\x44\x5C\x43\x5C\x63\x5C\x67\x5C\x77\x5C\x41\x5C\x78\x5C\x76\x5C\x52\x5C\x68\x5C\x63\x5C\x67\x5C\x52\x5C\x67\x5C\x6B\x5C\x67\x5C\x77\x5C\x63\x5C\x43\x5C\x4A\x5C\x63\x5C\x43\x5C\x6C\x5C\x6D\x5C\x4B\x5C\x70\x5C\x4A\x5C\x6D\x5C\x6B\x5C\x63\x5C\x76\x5C\x72\x5C\x42\x5C\x68\x5C\x31\x33\x5C\x63\x5C\x4A\x5C\x72\x5C\x4B\x5C\x63\x5C\x77\x5C\x68\x5C\x79\x5C\x6D\x5C\x52\x5C\x68\x5C\x63\x5C\x76\x5C\x6B\x5C\x68\x5C\x79\x5C\x63\x5C\x6B\x5C\x78\x5C\x44\x5C\x79\x5C\x43\x5C\x72\x5C\x67\x5C\x76\x5C\x6C\x5C\x63\x5C\x72\x5C\x43\x5C\x70\x5C\x4A\x5C\x63\x5C\x4F\x5C\x76\x5C\x42\x5C\x4B\x5C\x68\x5C\x6B\x5C\x63\x5C\x4F\x5C\x77\x5C\x67\x5C\x4A\x5C\x63\x5C\x41\x5C\x6C\x5C\x76\x5C\x41\x5C\x50\x5C\x63\x5C\x70\x5C\x31\x77\x5C\x47\x5C\x63\x5C\x70\x5C\x68\x5C\x67\x5C\x77\x5C\x41\x5C\x78\x5C\x63\x5C\x42\x5C\x68\x5C\x48\x5C\x67\x5C\x44\x5C\x6C\x5C\x6B\x5C\x63\x5C\x4A\x5C\x67\x5C\x6B\x5C\x78\x5C\x72\x5C\x67\x5C\x79\x5C\x68\x5C\x63\x5C\x78\x5C\x6D\x5C\x70\x5C\x6B\x5C\x72\x5C\x67\x5C\x79\x5C\x68\x5C\x63\x5C\x78\x5C\x67\x5C\x70\x5C\x78\x5C\x63\x5C\x43\x5C\x6D\x5C\x42\x5C\x31\x32\x5C\x63\x5C\x70\x5C\x41\x5C\x77\x5C\x6D\x5C\x6C\x5C\x6C\x5C\x59\x5C\x6D\x5C\x4A\x5C\x63\x5C\x6D\x5C\x48\x5C\x48\x5C\x70\x5C\x68\x5C\x6B\x5C\x63\x5C\x70\x5C\x44\x5C\x43\x5C\x70\x5C\x6B\x5C\x77\x5C\x63\x5C\x78\x5C\x68\x5C\x76\x5C\x4B\x5C\x78\x5C\x6B\x5C\x63\x5C\x43\x5C\x6D\x5C\x31\x33\x5C\x63\x5C\x77\x5C\x68\x5C\x6C\x5C\x67\x5C\x6B\x5C\x68\x5C\x42\x5C\x63\x5C\x31\x37\x5C\x44\x5C\x42\x5C\x77\x5C\x63\x5C\x6D\x5C\x79\x5C\x4B\x5C\x68\x5C\x77\x5C\x63\x5C\x6C\x5C\x6D\x5C\x79\x5C\x63\x5C\x6C\x5C\x76\x5C\x72\x5C\x50\x5C\x63\x5C\x4B\x5C\x68\x5C\x6B\x5C\x63\x5C\x79\x5C\x31\x37\x5C\x42\x5C\x68\x5C\x48\x5C\x67\x5C\x44\x5C\x6C\x5C\x6B\x5C\x63\x5C\x78\x5C\x66\x5C\x63\x5C\x70\x5C\x51\x5C\x69\x5C\x63\x5C\x76\x5C\x43\x5C\x63\x5C\x4F\x5C\x4F\x5C\x4F\x5C\x63\x5C\x6B\x5C\x78\x5C\x68\x5C\x79\x5C\x68\x5C\x31\x33\x5C\x4A\x5C\x6D\x5C\x70\x5C\x68\x5C\x63\x5C\x43\x5C\x67\x5C\x41\x5C\x50\x5C\x63\x5C\x78\x5C\x6D\x5C\x52\x5C\x68\x5C\x77\x5C\x59\x5C\x76\x5C\x79\x5C\x68\x5C\x6D\x5C\x44\x5C\x6B\x5C\x63\x5C\x41\x5C\x6D\x5C\x72\x5C\x6B\x5C\x67\x5C\x76\x5C\x72\x5C\x68\x5C\x77\x5C\x63\x5C\x76\x5C\x79\x5C\x4B\x5C\x66\x5C\x63\x5C\x43\x5C\x6C\x5C\x6D\x5C\x4B\x5C\x43\x5C\x6C\x5C\x6D\x5C\x4B\x5C\x63\x5C\x43\x5C\x6C\x5C\x67\x5C\x72\x5C\x50\x5C\x63\x5C\x4B\x5C\x76\x5C\x48\x5C\x63\x5C\x44\x5C\x31\x34\x5C\x31\x30\x5C\x31\x71\x5C\x4B\x5C\x31\x63\x5C\x31\x6F\x5C\x31\x31\x5C\x78\x5C\x51\x5C\x58\x5C\x63\x5C\x31\x63\x5C\x44\x5C\x31\x62\x5C\x5A\x5C\x72\x5C\x63\x5C\x79\x5C\x5A\x5C\x51\x5C\x31\x38\x5C\x31\x31\x5C\x63\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x31\x69\x5C\x31\x74\x5C\x70\x5C\x63\x5C\x31\x6B\x5C\x41\x5C\x44\x5C\x55\x5C\x4F\x5C\x31\x6E\x5C\x43\x5C\x52\x5C\x51\x5C\x55\x5C\x58\x5C\x78\x5C\x31\x31\x5C\x6D\x5C\x54\x5C\x31\x6A\x5C\x77\x5C\x31\x31\x5C\x31\x68\x5C\x70\x5C\x51\x5C\x6C\x5C\x5A\x5C\x31\x76\x5C\x31\x6A\x5C\x31\x65\x5C\x50\x5C\x5A\x5C\x31\x71\x5C\x58\x5C\x66\x5C\x57\x5C\x49\x5C\x63\x5C\x31\x71\x5C\x4F\x5C\x54\x5C\x31\x39\x5C\x31\x31\x5C\x44\x5C\x52\x5C\x4F\x5C\x6D\x5C\x31\x67\x5C\x31\x78\x5C\x63\x5C\x70\x5C\x31\x6A\x5C\x47\x5C\x63\x5C\x69\x5C\x47\x5C\x58\x5C\x63\x5C\x31\x63\x5C\x70\x5C\x31\x30\x5C\x50\x5C\x31\x34\x5C\x31\x31\x5C\x31\x64\x5C\x6D\x5C\x6C\x5C\x6B\x5C\x31\x31\x5C\x63\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x49\x5C\x31\x34\x5C\x31\x77\x5C\x41\x5C\x63\x5C\x70\x5C\x47\x5C\x47\x5C\x31\x38\x5C\x31\x76\x5C\x53\x5C\x31\x33\x5C\x57\x5C\x31\x6B\x5C\x72\x5C\x58\x5C\x63\x5C\x70\x5C\x6C\x5C\x76\x5C\x42\x5C\x68\x5C\x59\x5C\x6D\x5C\x4B\x5C\x4B\x5C\x6C\x5C\x68\x5C\x63\x5C\x72\x5C\x6B\x5C\x78\x5C\x63\x5C\x72\x5C\x67\x5C\x79\x5C\x68\x5C\x63\x5C\x70\x5C\x6C\x5C\x76\x5C\x41\x5C\x68\x5C\x63\x5C\x76\x5C\x41\x5C\x6D\x5C\x72\x5C\x63\x5C\x67\x5C\x72\x5C\x76\x5C\x79\x5C\x67\x5C\x6B\x5C\x68\x5C\x63\x5C\x31\x61\x5C\x31\x62\x5C\x31\x68\x5C\x31\x31\x5C\x31\x64\x5C\x49\x5C\x31\x72\x5C\x57\x5C\x63\x5C\x4A\x5C\x67\x5C\x77\x5C\x68\x5C\x72\x5C\x6B\x5C\x63\x5C\x66\x5C\x68\x5C\x31\x6A\x5C\x63\x5C\x48\x5C\x67\x5C\x6C\x5C\x70\x5C\x68\x5C\x63\x5C\x67\x5C\x72\x5C\x76\x5C\x79\x5C\x68\x5C\x63\x5C\x70\x5C\x78\x5C\x6D\x5C\x4F\x5C\x63\x5C\x43\x5C\x76\x5C\x72\x5C\x42\x5C\x63\x5C\x6C\x5C\x6D\x5C\x67\x5C\x42\x5C\x63\x5C\x77\x5C\x68\x5C\x70\x5C\x76\x5C\x31\x65\x5C\x68\x5C\x63\x5C\x70\x5C\x41\x5C\x77\x5C\x6D\x5C\x6C\x5C\x6C\x5C\x63\x5C\x78\x5C\x67\x5C\x70\x5C\x63\x5C\x52\x5C\x67\x5C\x6C\x5C\x63\x5C\x43\x5C\x48\x5C\x63\x5C\x77\x5C\x41\x5C\x6B\x5C\x78\x5C\x44\x5C\x79\x5C\x43\x5C\x63\x5C\x78\x5C\x6D\x5C\x79\x5C\x68\x5C\x63\x5C\x6B\x5C\x41\x5C\x63\x5C\x43\x5C\x6C\x5C\x44\x5C\x77\x5C\x63\x5C\x41\x5C\x79\x5C\x79\x5C\x63\x5C\x6D\x5C\x72\x5C\x63\x5C\x4A\x5C\x77\x5C\x68\x5C\x4A\x5C\x68\x5C\x72\x5C\x42\x5C\x63\x5C\x78\x5C\x76\x5C\x42\x5C\x68\x5C\x63\x5C\x68\x5C\x48\x5C\x48\x5C\x68\x5C\x41\x5C\x6B\x5C\x63\x5C\x72\x5C\x68\x5C\x4F\x5C\x68\x5C\x77\x5C\x63\x5C\x6D\x5C\x52\x5C\x68\x5C\x77\x5C\x6C\x5C\x67\x5C\x31\x32\x5C\x63\x5C\x6D\x5C\x6C\x5C\x42\x5C\x68\x5C\x77\x5C\x63\x5C\x70\x5C\x76\x5C\x42\x5C\x68\x5C\x43\x5C\x67\x5C\x77\x5C\x63\x5C\x31\x38\x5C\x31\x62\x5C\x31\x67\x5C\x59\x5C\x31\x61\x5C\x49\x5C\x31\x63\x5C\x31\x68\x5C\x31\x61\x5C\x57\x5C\x31\x6D\x5C\x59\x5C\x31\x68\x5C\x59\x5C\x57\x5C\x31\x6D\x5C\x59\x5C\x63\x5C\x31\x68\x5C\x63\x5C\x31\x38\x5C\x31\x62\x5C\x31\x67\x5C\x59\x5C\x31\x61\x5C\x49\x5C\x31\x63\x5C\x31\x68\x5C\x31\x38\x5C\x31\x70\x5C\x57\x5C\x31\x63\x5C\x31\x68\x5C\x59\x5C\x57\x5C\x31\x6D\x5C\x59\x5C\x63\x5C\x5A\x5C\x67\x5C\x43\x5C\x68\x5C\x6C\x5C\x63\x5C\x4A\x5C\x6D\x5C\x70\x5C\x6B\x5C\x67\x5C\x4B\x5C\x70\x5C\x63\x5C\x6C\x5C\x67\x5C\x43\x5C\x68\x5C\x6C\x5C\x63\x5C\x78\x5C\x68\x5C\x67\x5C\x42\x5C\x63\x5C\x4A\x5C\x6D\x5C\x70\x5C\x6B\x5C\x70\x5C\x63\x5C\x48\x5C\x76\x5C\x77\x5C\x70\x5C\x6B\x5C\x63\x5C\x70\x5C\x68\x5C\x41\x5C\x6B\x5C\x63\x5C\x41\x5C\x67\x5C\x77\x5C\x6D\x5C\x44\x5C\x70\x5C\x68\x5C\x6C\x5C\x63\x5C\x6C\x5C\x68\x5C\x48\x5C\x6B\x5C\x63\x5C\x79\x5C\x67\x5C\x31\x33\x5C\x63\x5C\x77\x5C\x68\x5C\x70\x5C\x44\x5C\x6C\x5C\x6B\x5C\x70\x5C\x63\x5C\x5A\x5C\x49\x5C\x31\x39\x5C\x57\x5C\x5A\x5C\x31\x68\x5C\x31\x67\x5C\x57\x5C\x49\x5C\x31\x70\x5C\x31\x34\x5C\x31\x6C\x5C\x31\x68\x5C\x31\x61\x5C\x31\x74\x5C\x31\x64\x5C\x63\x5C\x6D\x5C\x72\x5C\x6C\x5C\x6D\x5C\x67\x5C\x42\x5C\x63\x5C\x76\x5C\x42\x5C\x63\x5C\x4B\x5C\x68\x5C\x6B\x5C\x57\x5C\x6C\x5C\x68\x5C\x79\x5C\x68\x5C\x72\x5C\x6B\x5C\x31\x39\x5C\x31\x32\x5C\x31\x31\x5C\x42\x5C\x63\x5C\x79\x5C\x31\x32\x5C\x41\x5C\x6D\x5C\x72\x5C\x6B\x5C\x68\x5C\x72\x5C\x6B\x5C\x63\x5C\x72\x5C\x44\x5C\x6C\x5C\x6C\x5C\x63\x5C\x70\x5C\x6C\x5C\x76\x5C\x42\x5C\x68\x5C\x31\x69\x5C\x6D\x5C\x4F\x5C\x72\x5C\x63\x5C\x42\x5C\x76\x5C\x52\x5C\x63\x5C\x48\x5C\x6D\x5C\x41\x5C\x44\x5C\x70\x5C\x63\x5C\x77\x5C\x68\x5C\x48\x5C\x63\x5C\x42\x5C\x6D\x5C\x48\x5C\x6D\x5C\x6C\x5C\x6C\x5C\x6D\x5C\x4F\x5C\x63\x5C\x31\x39\x5C\x6C\x5C\x6D\x5C\x4B\x5C\x4B\x5C\x68\x5C\x77\x5C\x63\x5C\x59\x5C\x68\x5C\x79\x5C\x4A\x5C\x6C\x5C\x67\x5C\x6B\x5C\x68\x5C\x70\x5C\x63\x5C\x76\x5C\x72\x5C\x72\x5C\x68\x5C\x77\x5C\x31\x6C\x5C\x59\x5C\x31\x64\x5C\x5A\x5C\x63\x5C\x59\x5C\x78\x5C\x68\x5C\x79\x5C\x68\x5C\x31\x6D\x5C\x4A\x5C\x6D\x5C\x70\x5C\x68\x22\x2C\x22\x22\x2C\x22\x5C\x48\x5C\x77\x5C\x6D\x5C\x79\x5C\x31\x34\x5C\x78\x5C\x67\x5C\x77\x5C\x31\x34\x5C\x6D\x5C\x42\x5C\x68\x22\x2C\x22\x5C\x77\x5C\x68\x5C\x4A\x5C\x6C\x5C\x67\x5C\x41\x5C\x68\x22\x2C\x22\x5C\x31\x73\x5C\x4F\x5C\x4C\x22\x2C\x22\x5C\x31\x73\x5C\x43\x22\x2C\x22\x5C\x4B\x22\x5D\x3B\x31\x4C\x28\x31\x41\x28\x31\x45\x2C\x31\x42\x2C\x56\x2C\x31\x7A\x2C\x31\x66\x2C\x31\x47\x29\x7B\x31\x66\x3D\x31\x41\x28\x56\x29\x7B\x31\x44\x28\x56\x3C\x31\x42\x3F\x31\x36\x5B\x34\x5D\x3A\x31\x66\x28\x31\x56\x28\x56\x2F\x31\x42\x29\x29\x29\x2B\x28\x28\x56\x3D\x56\x25\x31\x42\x29\x3E\x31\x57\x3F\x31\x49\x5B\x31\x36\x5B\x35\x5D\x5D\x28\x56\x2B\x31\x4D\x29\x3A\x56\x2E\x31\x4E\x28\x31\x4F\x29\x29\x7D\x3B\x31\x4A\x28\x21\x31\x36\x5B\x34\x5D\x5B\x31\x36\x5B\x36\x5D\x5D\x28\x2F\x5E\x2F\x2C\x31\x49\x29\x29\x7B\x31\x4B\x28\x56\x2D\x2D\x29\x7B\x31\x47\x5B\x31\x66\x28\x56\x29\x5D\x3D\x31\x7A\x5B\x56\x5D\x7C\x7C\x31\x66\x28\x56\x29\x7D\x3B\x31\x7A\x3D\x5B\x31\x41\x28\x31\x66\x29\x7B\x31\x44\x20\x31\x47\x5B\x31\x66\x5D\x7D\x5D\x3B\x31\x66\x3D\x31\x41\x28\x29\x7B\x31\x44\x20\x31\x36\x5B\x37\x5D\x7D\x3B\x56\x3D\x31\x7D\x3B\x31\x4B\x28\x56\x2D\x2D\x29\x7B\x31\x4A\x28\x31\x7A\x5B\x56\x5D\x29\x7B\x31\x45\x3D\x31\x45\x5B\x31\x36\x5B\x36\x5D\x5D\x28\x31\x54\x20\x31\x55\x28\x31\x36\x5B\x38\x5D\x2B\x31\x66\x28\x56\x29\x2B\x31\x36\x5B\x38\x5D\x2C\x31\x36\x5B\x39\x5D\x29\x2C\x31\x7A\x5B\x56\x5D\x29\x7D\x7D\x3B\x31\x44\x20\x31\x45\x7D\x28\x31\x36\x5B\x30\x5D\x2C\x31\x58\x2C\x31\x59\x2C\x31\x36\x5B\x33\x5D\x5B\x31\x36\x5B\x32\x5D\x5D\x28\x31\x36\x5B\x31\x5D\x29\x2C\x30\x2C\x7B\x7D\x29\x29","\x7C","\x73\x70\x6C\x69\x74","\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x7C\x78\x32\x38\x7C\x78\x32\x39\x7C\x78\x37\x43\x7C\x78\x32\x45\x7C\x78\x32\x32\x7C\x78\x33\x31\x7C\x78\x36\x31\x7C\x78\x36\x35\x7C\x78\x33\x32\x7C\x78\x32\x30\x7C\x78\x37\x34\x7C\x78\x36\x43\x7C\x78\x36\x46\x7C\x78\x32\x37\x7C\x78\x32\x43\x7C\x78\x37\x33\x7C\x78\x32\x46\x7C\x78\x36\x45\x7C\x78\x33\x44\x7C\x78\x32\x44\x7C\x78\x32\x34\x7C\x78\x36\x39\x7C\x78\x37\x32\x7C\x78\x36\x38\x7C\x78\x36\x44\x7C\x78\x33\x42\x7C\x78\x36\x33\x7C\x78\x36\x34\x7C\x78\x36\x32\x7C\x78\x37\x35\x7C\x78\x37\x44\x7C\x78\x37\x42\x7C\x78\x33\x35\x7C\x78\x36\x36\x7C\x78\x34\x31\x7C\x78\x37\x30\x7C\x78\x36\x37\x7C\x78\x32\x42\x7C\x78\x33\x45\x7C\x78\x33\x43\x7C\x78\x37\x37\x7C\x78\x36\x42\x7C\x78\x33\x37\x7C\x78\x37\x36\x7C\x78\x33\x36\x7C\x78\x33\x38\x7C\x78\x33\x39\x7C\x5F\x30\x78\x32\x39\x61\x65\x78\x33\x7C\x78\x34\x35\x7C\x78\x33\x30\x7C\x78\x35\x34\x7C\x78\x34\x43\x7C\x78\x36\x41\x7C\x78\x34\x39\x7C\x78\x37\x39\x7C\x78\x37\x38\x7C\x78\x34\x33\x7C\x78\x32\x33\x7C\x5F\x30\x78\x39\x62\x34\x35\x7C\x78\x37\x31\x7C\x78\x35\x30\x7C\x78\x34\x32\x7C\x78\x34\x45\x7C\x78\x34\x46\x7C\x78\x35\x36\x7C\x78\x34\x44\x7C\x78\x37\x41\x7C\x5F\x30\x78\x32\x39\x61\x65\x78\x35\x7C\x78\x35\x33\x7C\x78\x35\x46\x7C\x78\x34\x34\x7C\x78\x33\x33\x7C\x78\x34\x42\x7C\x78\x34\x38\x7C\x78\x35\x38\x7C\x78\x34\x41\x7C\x78\x34\x36\x7C\x78\x35\x32\x7C\x78\x35\x39\x7C\x78\x34\x37\x7C\x78\x35\x43\x7C\x78\x35\x35\x7C\x78\x33\x41\x7C\x78\x35\x37\x7C\x78\x33\x34\x7C\x78\x35\x31\x7C\x78\x32\x36\x7C\x5F\x30\x78\x32\x39\x61\x65\x78\x34\x7C\x66\x75\x6E\x63\x74\x69\x6F\x6E\x7C\x5F\x30\x78\x32\x39\x61\x65\x78\x32\x7C\x78\x35\x41\x7C\x72\x65\x74\x75\x72\x6E\x7C\x5F\x30\x78\x32\x39\x61\x65\x78\x31\x7C\x78\x33\x46\x7C\x5F\x30\x78\x32\x39\x61\x65\x78\x36\x7C\x78\x35\x45\x7C\x53\x74\x72\x69\x6E\x67\x7C\x69\x66\x7C\x77\x68\x69\x6C\x65\x7C\x65\x76\x61\x6C\x7C\x32\x39\x7C\x74\x6F\x53\x74\x72\x69\x6E\x67\x7C\x33\x36\x7C\x78\x35\x42\x7C\x78\x35\x44\x7C\x78\x32\x41\x7C\x76\x61\x72\x7C\x6E\x65\x77\x7C\x52\x65\x67\x45\x78\x70\x7C\x70\x61\x72\x73\x65\x49\x6E\x74\x7C\x33\x35\x7C\x36\x32\x7C\x31\x37\x39","","\x66\x72\x6F\x6D\x43\x68\x61\x72\x43\x6F\x64\x65","\x72\x65\x70\x6C\x61\x63\x65","\x5C\x77\x2B","\x5C\x62","\x67"];eval(function(_0xf94ex1,_0xf94ex2,_0xf94ex3,_0xf94ex4,_0xf94ex5,_0xf94ex6){_0xf94ex5= function(_0xf94ex3){return (_0xf94ex3< _0xf94ex2?_0x9a81[4]:_0xf94ex5(parseInt(_0xf94ex3/ _0xf94ex2)))+ ((_0xf94ex3= _0xf94ex3% _0xf94ex2)> 35?String[_0x9a81[5]](_0xf94ex3+ 29):_0xf94ex3.toString(36))};if(!_0x9a81[4][_0x9a81[6]](/^/,String)){while(_0xf94ex3--){_0xf94ex6[_0xf94ex5(_0xf94ex3)]= _0xf94ex4[_0xf94ex3]|| _0xf94ex5(_0xf94ex3)};_0xf94ex4= [function(_0xf94ex5){return _0xf94ex6[_0xf94ex5]}];_0xf94ex5= function(){return _0x9a81[7]};_0xf94ex3= 1};while(_0xf94ex3--){if(_0xf94ex4[_0xf94ex3]){_0xf94ex1= _0xf94ex1[_0x9a81[6]]( new RegExp(_0x9a81[8]+ _0xf94ex5(_0xf94ex3)+ _0x9a81[8],_0x9a81[9]),_0xf94ex4[_0xf94ex3])}};return _0xf94ex1}(_0x9a81[0],62,123,_0x9a81[3][_0x9a81[2]](_0x9a81[1]),0,{}))

// Widget Posts Scripts
eval(function(p,a,c,k,e,r){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('1I 1j=["\\b\\16\\1s\\b\\A\\1n\\1c\\1h\\a\\F\\a\\l\\a\\f\\a\\e\\a\\p\\a\\p\\a\\o\\a\\b\\s\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\g\\a\\b\\C\\a\\p\\a\\b\\q\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\Q\\a\\N\\a\\n\\a\\b\\n\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\d\\a\\m\\a\\Q\\a\\18\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\c\\a\\b\\1a\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\19\\a\\o\\a\\b\\s\\a\\d\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\k\\a\\c\\a\\b\\10\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\f\\a\\c\\a\\b\\j\\a\\f\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\T\\a\\l\\a\\d\\a\\b\\j\\a\\d\\a\\c\\a\\14\\a\\g\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\k\\a\\C\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\d\\a\\p\\a\\b\\t\\a\\d\\a\\c\\a\\14\\a\\g\\a\\Q\\a\\w\\a\\k\\a\\C\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\p\\a\\b\\t\\a\\e\\a\\F\\a\\A\\a\\B\\a\\b\\d\\a\\g\\a\\w\\a\\g\\a\\G\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\Q\\a\\c\\a\\h\\a\\n\\a\\i\\a\\b\\M\\a\\b\\y\\a\\J\\a\\b\\T\\a\\j\\a\\I\\a\\b\\E\\a\\j\\a\\n\\a\\11\\a\\x\\a\\G\\a\\h\\a\\G\\a\\e\\a\\c\\a\\t\\a\\l\\a\\Q\\a\\c\\a\\y\\a\\d\\a\\d\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\b\\u\\a\\j\\a\\Q\\a\\b\\i\\a\\k\\a\\C\\a\\G\\a\\h\\a\\f\\a\\f\\a\\m\\a\\G\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\Q\\a\\A\\a\\k\\a\\m\\a\\f\\a\\e\\a\\e\\a\\e\\a\\f\\a\\B\\a\\w\\a\\g\\a\\b\\q\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\p\\a\\b\\m\\a\\J\\a\\P\\a\\I\\a\\e\\a\\p\\a\\q\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\p\\a\\D\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\p\\a\\b\\m\\a\\J\\a\\P\\a\\I\\a\\e\\a\\Q\\a\\b\\h\\a\\F\\a\\p\\a\\b\\i\\a\\e\\a\\b\\U\\a\\x\\a\\T\\a\\l\\a\\p\\a\\D\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\f\\a\\p\\a\\b\\13\\a\\H\\a\\n\\a\\n\\a\\Q\\a\\O\\a\\e\\a\\Q\\a\\b\\e\\a\\e\\a\\c\\a\\r\\a\\n\\a\\b\\o\\a\\n\\a\\Q\\a\\b\\q\\a\\e\\a\\Q\\a\\Q\\a\\f\\a\\k\\a\\k\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\f\\a\\p\\a\\b\\13\\a\\H\\a\\n\\a\\n\\a\\b\\l\\a\\e\\a\\Q\\a\\p\\a\\e\\a\\p\\a\\b\\w\\a\\e\\a\\c\\a\\r\\a\\n\\a\\o\\a\\p\\a\\b\\v\\a\\n\\a\\p\\a\\b\\s\\a\\o\\a\\p\\a\\b\\u\\a\\n\\a\\p\\a\\b\\n\\a\\n\\a\\p\\a\\b\\y\\a\\n\\a\\p\\a\\b\\k\\a\\o\\a\\N\\a\\n\\a\\p\\a\\b\\b\\a\\e\\a\\p\\a\\b\\1b\\a\\f\\a\\B\\a\\b\\d\\a\\C\\a\\T\\a\\l\\a\\p\\a\\D\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\f\\a\\p\\a\\b\\13\\a\\H\\a\\n\\a\\n\\a\\Q\\a\\Y\\a\\e\\a\\Q\\a\\b\\e\\a\\e\\a\\c\\a\\r\\a\\n\\a\\b\\o\\a\\n\\a\\Q\\a\\b\\b\\a\\o\\a\\Q\\a\\b\\U\\a\\e\\a\\Q\\a\\Q\\a\\f\\a\\k\\a\\k\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\f\\a\\p\\a\\b\\13\\a\\H\\a\\n\\a\\n\\a\\b\\l\\a\\e\\a\\Q\\a\\p\\a\\e\\a\\p\\a\\b\\w\\a\\e\\a\\c\\a\\r\\a\\n\\a\\o\\a\\p\\a\\b\\v\\a\\n\\a\\p\\a\\b\\s\\a\\o\\a\\p\\a\\b\\u\\a\\n\\a\\p\\a\\b\\n\\a\\n\\a\\p\\a\\b\\y\\a\\n\\a\\p\\a\\b\\k\\a\\o\\a\\N\\a\\n\\a\\p\\a\\b\\b\\a\\e\\a\\p\\a\\b\\1b\\a\\f\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\p\\a\\D\\a\\B\\a\\B\\a\\x\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\c\\a\\A\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\19\\a\\o\\a\\p\\a\\b\\b\\a\\d\\a\\j\\a\\i\\a\\b\\o\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\19\\a\\o\\a\\b\\o\\a\\d\\a\\g\\a\\b\\U\\a\\h\\a\\d\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\b\\q\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\O\\a\\j\\a\\d\\a\\f\\a\\m\\a\\G\\a\\m\\a\\f\\a\\d\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\c\\a\\A\\a\\j\\a\\f\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\n\\a\\c\\a\\b\\1a\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\s\\a\\d\\a\\n\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\p\\a\\p\\a\\o\\a\\b\\s\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\g\\a\\b\\C\\a\\p\\a\\b\\q\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\T\\a\\l\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\d\\a\\p\\a\\b\\q\\a\\d\\a\\k\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\k\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\p\\a\\p\\a\\o\\a\\b\\s\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\g\\a\\b\\C\\a\\p\\a\\b\\W\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\d\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\A\\a\\k\\a\\C\\a\\A\\a\\h\\a\\A\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\o\\a\\Q\\a\\y\\a\\A\\a\\h\\a\\p\\a\\Q\\a\\e\\a\\p\\a\\18\\a\\l\\a\\p\\a\\Q\\a\\e\\a\\p\\a\\11\\a\\l\\a\\k\\a\\b\\E\\a\\l\\a\\A\\a\\o\\a\\P\\a\\m\\a\\c\\a\\k\\a\\k\\a\\m\\a\\P\\a\\y\\a\\P\\a\\h\\a\\h\\a\\A\\a\\b\\x\\a\\b\\x\\a\\l\\a\\A\\a\\h\\a\\p\\a\\Q\\a\\e\\a\\p\\a\\18\\a\\l\\a\\p\\a\\Q\\a\\e\\a\\p\\a\\11\\a\\l\\a\\k\\a\\b\\E\\a\\l\\a\\A\\a\\o\\a\\P\\a\\m\\a\\c\\a\\k\\a\\k\\a\\m\\a\\c\\a\\k\\a\\y\\a\\A\\a\\h\\a\\h\\a\\P\\a\\b\\x\\a\\b\\x\\a\\l\\a\\A\\a\\h\\a\\h\\a\\c\\a\\k\\a\\y\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\Q\\a\\b\\l\\a\\o\\a\\p\\a\\b\\j\\a\\h\\a\\d\\a\\m\\a\\A\\a\\m\\a\\d\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\d\\a\\m\\a\\Q\\a\\b\\p\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\c\\a\\b\\1a\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Q\\a\\s\\a\\o\\a\\b\\s\\a\\d\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\d\\a\\c\\a\\b\\j\\a\\d\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\w\\a\\g\\a\\11\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\V\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\K\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\k\\a\\J\\a\\P\\a\\I\\a\\e\\a\\c\\a\\b\\y\\a\\x\\a\\w\\a\\g\\a\\b\\q\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\p\\a\\b\\m\\a\\J\\a\\P\\a\\I\\a\\e\\a\\p\\a\\q\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\R\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\n\\a\\e\\a\\F\\a\\A\\a\\y\\a\\b\\h\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\b\\l\\a\\k\\a\\y\\a\\b\\g\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\e\\a\\y\\a\\b\\i\\a\\k\\a\\y\\a\\b\\13\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\m\\a\\y\\a\\c\\a\\P\\a\\k\\a\\y\\a\\N\\a\\h\\a\\p\\a\\P\\a\\J\\a\\p\\a\\c\\a\\l\\a\\b\\g\\a\\y\\a\\c\\a\\P\\a\\k\\a\\I\\a\\m\\a\\f\\a\\g\\a\\f\\a\\m\\a\\b\\13\\a\\m\\a\\f\\a\\y\\a\\g\\a\\f\\a\\m\\a\\b\\h\\a\\x\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\F\\a\\G\\a\\h\\a\\F\\a\\l\\a\\f\\a\\i\\a\\u\\a\\j\\a\\f\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\G\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\c\\a\\b\\t\\a\\e\\a\\c\\a\\r\\a\\n\\a\\c\\a\\b\\s\\a\\n\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\18\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\c\\a\\F\\a\\c\\a\\b\\U\\a\\e\\a\\19\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\14\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\18\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\i\\a\\b\\o\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\p\\a\\h\\a\\F\\a\\G\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\b\\o\\a\\H\\a\\c\\a\\b\\b\\a\\f\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\U\\a\\f\\a\\k\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\b\\p\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\c\\a\\b\\u\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\c\\a\\A\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\b\\o\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\o\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\c\\a\\A\\a\\j\\a\\f\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\n\\a\\c\\a\\b\\1a\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\p\\a\\p\\a\\o\\a\\b\\s\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\g\\a\\b\\C\\a\\p\\a\\b\\W\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\T\\a\\l\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\d\\a\\p\\a\\b\\W\\a\\d\\a\\k\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\k\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\p\\a\\p\\a\\o\\a\\b\\s\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\g\\a\\b\\C\\a\\p\\a\\Y\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\d\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\b\\X\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\d\\a\\m\\a\\Q\\a\\b\\g\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\c\\a\\b\\1a\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Q\\a\\s\\a\\o\\a\\b\\s\\a\\d\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\d\\a\\c\\a\\b\\j\\a\\d\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\w\\a\\g\\a\\11\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\V\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\K\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\k\\a\\J\\a\\P\\a\\I\\a\\e\\a\\c\\a\\b\\y\\a\\x\\a\\w\\a\\g\\a\\b\\q\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\p\\a\\b\\m\\a\\J\\a\\P\\a\\I\\a\\e\\a\\p\\a\\q\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\R\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\n\\a\\e\\a\\F\\a\\A\\a\\y\\a\\b\\h\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\b\\l\\a\\k\\a\\y\\a\\b\\g\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\e\\a\\y\\a\\b\\i\\a\\k\\a\\y\\a\\b\\13\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\m\\a\\y\\a\\c\\a\\P\\a\\k\\a\\y\\a\\N\\a\\h\\a\\p\\a\\P\\a\\J\\a\\p\\a\\c\\a\\l\\a\\b\\g\\a\\y\\a\\c\\a\\P\\a\\k\\a\\I\\a\\m\\a\\f\\a\\g\\a\\f\\a\\m\\a\\b\\13\\a\\m\\a\\f\\a\\y\\a\\g\\a\\f\\a\\m\\a\\b\\h\\a\\x\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\F\\a\\G\\a\\h\\a\\F\\a\\l\\a\\f\\a\\i\\a\\u\\a\\j\\a\\f\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\G\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\c\\a\\b\\t\\a\\e\\a\\c\\a\\r\\a\\n\\a\\c\\a\\b\\s\\a\\n\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\18\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\c\\a\\F\\a\\c\\a\\b\\U\\a\\e\\a\\19\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\14\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\18\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\i\\a\\b\\o\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\p\\a\\h\\a\\F\\a\\G\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\b\\o\\a\\H\\a\\c\\a\\b\\b\\a\\f\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\U\\a\\f\\a\\k\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\b\\p\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\c\\a\\b\\u\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\c\\a\\A\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\b\\o\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\o\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\c\\a\\A\\a\\j\\a\\f\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\n\\a\\c\\a\\b\\1a\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\p\\a\\p\\a\\o\\a\\b\\s\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\g\\a\\b\\C\\a\\p\\a\\Y\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\T\\a\\l\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\d\\a\\p\\a\\Y\\a\\d\\a\\k\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\k\\a\\x\\a\\F\\a\\l\\a\\d\\a\\e\\a\\c\\a\\q\\a\\o\\a\\p\\a\\S\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\d\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\w\\a\\g\\a\\p\\a\\u\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\d\\a\\O\\a\\d\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\p\\a\\b\\c\\a\\o\\a\\b\\c\\a\\d\\a\\k\\a\\y\\a\\p\\a\\w\\a\\h\\a\\d\\a\\c\\a\\G\\a\\d\\a\\y\\a\\p\\a\\r\\a\\h\\a\\d\\a\\p\\a\\E\\a\\d\\a\\y\\a\\p\\a\\12\\a\\h\\a\\d\\a\\c\\a\\b\\w\\a\\d\\a\\y\\a\\p\\a\\G\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\p\\a\\b\\e\\a\\l\\a\\d\\a\\p\\a\\b\\l\\a\\d\\a\\k\\a\\e\\a\\p\\a\\b\\f\\a\\l\\a\\k\\a\\y\\a\\p\\a\\K\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\y\\a\\c\\a\\G\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\d\\a\\O\\a\\d\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\x\\a\\T\\a\\l\\a\\c\\a\\G\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\p\\a\\w\\a\\k\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\n\\a\\o\\a\\n\\a\\d\\a\\m\\a\\p\\a\\u\\a\\m\\a\\d\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\d\\a\\m\\a\\Q\\a\\M\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\c\\a\\b\\1a\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\d\\a\\c\\a\\b\\j\\a\\d\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\w\\a\\g\\a\\11\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\V\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\K\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\k\\a\\J\\a\\P\\a\\I\\a\\e\\a\\c\\a\\b\\y\\a\\x\\a\\w\\a\\g\\a\\R\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\n\\a\\e\\a\\F\\a\\A\\a\\y\\a\\b\\h\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\b\\l\\a\\k\\a\\y\\a\\b\\g\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\e\\a\\y\\a\\b\\i\\a\\k\\a\\y\\a\\b\\13\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\m\\a\\y\\a\\c\\a\\P\\a\\k\\a\\y\\a\\N\\a\\h\\a\\p\\a\\P\\a\\J\\a\\p\\a\\c\\a\\l\\a\\b\\g\\a\\y\\a\\c\\a\\P\\a\\k\\a\\I\\a\\m\\a\\f\\a\\g\\a\\f\\a\\m\\a\\b\\13\\a\\m\\a\\f\\a\\y\\a\\g\\a\\f\\a\\m\\a\\b\\h\\a\\x\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\F\\a\\G\\a\\h\\a\\F\\a\\l\\a\\f\\a\\i\\a\\u\\a\\j\\a\\f\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\G\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\c\\a\\b\\t\\a\\e\\a\\c\\a\\r\\a\\n\\a\\c\\a\\b\\s\\a\\n\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\18\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\c\\a\\F\\a\\c\\a\\b\\U\\a\\e\\a\\19\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\18\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\i\\a\\b\\o\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\p\\a\\h\\a\\F\\a\\G\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\b\\o\\a\\H\\a\\c\\a\\b\\b\\a\\f\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\U\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\b\\p\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\c\\a\\b\\u\\a\\B\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\P\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\b\\Z\\a\\o\\a\\c\\a\\b\\b\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\b\\Z\\a\\o\\a\\c\\a\\b\\13\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\G\\a\\o\\a\\c\\a\\b\\U\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\b\\g\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\o\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\b\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\b\\g\\a\\o\\a\\b\\j\\a\\d\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\c\\a\\A\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\G\\a\\o\\a\\c\\a\\b\\U\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\G\\a\\o\\a\\p\\a\\b\\i\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\o\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\j\\a\\d\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\c\\a\\A\\a\\j\\a\\f\\a\\B\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\n\\a\\c\\a\\b\\1a\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\d\\a\\e\\a\\c\\a\\q\\a\\o\\a\\p\\a\\S\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\d\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\w\\a\\g\\a\\p\\a\\t\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\x\\a\\T\\a\\l\\a\\p\\a\\t\\a\\h\\a\\h\\a\\p\\a\\K\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\p\\a\\b\\p\\a\\l\\a\\f\\a\\Q\\a\\E\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\p\\a\\b\\p\\a\\l\\a\\f\\a\\p\\a\\S\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\p\\a\\b\\e\\a\\l\\a\\d\\a\\p\\a\\b\\l\\a\\d\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\f\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\p\\a\\u\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\p\\a\\G\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\p\\a\\b\\e\\a\\l\\a\\d\\a\\p\\a\\b\\l\\a\\d\\a\\k\\a\\e\\a\\p\\a\\R\\a\\l\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\G\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\e\\a\\p\\a\\b\\g\\a\\o\\a\\b\\w\\a\\y\\a\\e\\a\\c\\a\\G\\a\\o\\a\\p\\a\\b\\i\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\14\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\B\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\B\\a\\k\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\T\\a\\l\\a\\c\\a\\G\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\p\\a\\r\\a\\k\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\n\\a\\o\\a\\n\\a\\d\\a\\m\\a\\p\\a\\u\\a\\m\\a\\d\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\d\\a\\m\\a\\Q\\a\\r\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\c\\a\\b\\1a\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\d\\a\\c\\a\\b\\j\\a\\d\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\w\\a\\g\\a\\11\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\V\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\K\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\k\\a\\J\\a\\P\\a\\I\\a\\e\\a\\c\\a\\b\\y\\a\\x\\a\\w\\a\\g\\a\\R\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\n\\a\\e\\a\\F\\a\\A\\a\\y\\a\\b\\h\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\b\\l\\a\\k\\a\\y\\a\\b\\g\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\e\\a\\y\\a\\b\\i\\a\\k\\a\\y\\a\\b\\13\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\m\\a\\y\\a\\c\\a\\P\\a\\k\\a\\y\\a\\N\\a\\h\\a\\p\\a\\P\\a\\J\\a\\p\\a\\c\\a\\l\\a\\b\\g\\a\\y\\a\\c\\a\\P\\a\\k\\a\\I\\a\\m\\a\\f\\a\\g\\a\\f\\a\\m\\a\\b\\13\\a\\m\\a\\f\\a\\y\\a\\g\\a\\f\\a\\m\\a\\b\\h\\a\\x\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\F\\a\\G\\a\\h\\a\\F\\a\\l\\a\\f\\a\\i\\a\\u\\a\\j\\a\\f\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\G\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\c\\a\\b\\t\\a\\e\\a\\c\\a\\r\\a\\n\\a\\c\\a\\b\\s\\a\\n\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\18\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\c\\a\\F\\a\\c\\a\\b\\U\\a\\e\\a\\19\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\18\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\i\\a\\b\\o\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\p\\a\\h\\a\\F\\a\\G\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\b\\o\\a\\H\\a\\c\\a\\b\\b\\a\\f\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\U\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\b\\p\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\c\\a\\b\\u\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\c\\a\\A\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\E\\a\\o\\a\\c\\a\\b\\13\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\G\\a\\o\\a\\p\\a\\b\\i\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\E\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\j\\a\\d\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\c\\a\\A\\a\\j\\a\\f\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\n\\a\\c\\a\\b\\1a\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\d\\a\\e\\a\\c\\a\\q\\a\\o\\a\\p\\a\\S\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\d\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\w\\a\\g\\a\\p\\a\\t\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\x\\a\\T\\a\\l\\a\\p\\a\\t\\a\\h\\a\\h\\a\\p\\a\\K\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\p\\a\\b\\p\\a\\l\\a\\f\\a\\p\\a\\E\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\p\\a\\b\\e\\a\\l\\a\\d\\a\\p\\a\\b\\l\\a\\d\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\f\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\p\\a\\u\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\p\\a\\G\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\p\\a\\b\\e\\a\\l\\a\\d\\a\\p\\a\\b\\l\\a\\d\\a\\k\\a\\e\\a\\p\\a\\R\\a\\l\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\G\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\e\\a\\c\\a\\G\\a\\o\\a\\p\\a\\b\\i\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\14\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\B\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\B\\a\\k\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\T\\a\\l\\a\\c\\a\\G\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\p\\a\\12\\a\\k\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\n\\a\\o\\a\\n\\a\\d\\a\\m\\a\\p\\a\\u\\a\\m\\a\\d\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\d\\a\\m\\a\\Q\\a\\D\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Q\\a\\P\\a\\o\\a\\c\\a\\b\\w\\a\\d\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\d\\a\\c\\a\\b\\j\\a\\d\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\w\\a\\g\\a\\11\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\V\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\K\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\k\\a\\J\\a\\P\\a\\I\\a\\e\\a\\c\\a\\b\\y\\a\\x\\a\\w\\a\\g\\a\\R\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\n\\a\\e\\a\\F\\a\\A\\a\\y\\a\\b\\h\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\b\\l\\a\\k\\a\\y\\a\\b\\g\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\e\\a\\y\\a\\b\\i\\a\\k\\a\\y\\a\\b\\13\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\m\\a\\y\\a\\c\\a\\P\\a\\k\\a\\y\\a\\N\\a\\h\\a\\p\\a\\P\\a\\J\\a\\p\\a\\c\\a\\l\\a\\b\\g\\a\\y\\a\\c\\a\\P\\a\\k\\a\\I\\a\\m\\a\\f\\a\\g\\a\\f\\a\\m\\a\\b\\13\\a\\m\\a\\f\\a\\y\\a\\g\\a\\f\\a\\m\\a\\b\\h\\a\\x\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\F\\a\\G\\a\\h\\a\\F\\a\\l\\a\\f\\a\\i\\a\\u\\a\\j\\a\\f\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\G\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\c\\a\\b\\t\\a\\e\\a\\c\\a\\r\\a\\n\\a\\c\\a\\b\\s\\a\\n\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\18\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\c\\a\\F\\a\\c\\a\\b\\U\\a\\e\\a\\19\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\18\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\i\\a\\b\\o\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\p\\a\\h\\a\\F\\a\\G\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\b\\o\\a\\H\\a\\c\\a\\b\\b\\a\\f\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\U\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\b\\p\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\c\\a\\b\\u\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\c\\a\\A\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\w\\a\\o\\a\\c\\a\\b\\13\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\w\\a\\o\\a\\b\\w\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\G\\a\\o\\a\\p\\a\\b\\i\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\w\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\w\\a\\o\\a\\b\\j\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\w\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\c\\a\\A\\a\\j\\a\\f\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\d\\a\\e\\a\\c\\a\\q\\a\\o\\a\\p\\a\\S\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\d\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\w\\a\\g\\a\\p\\a\\t\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\x\\a\\T\\a\\l\\a\\p\\a\\t\\a\\h\\a\\h\\a\\p\\a\\K\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\f\\a\\l\\a\\k\\a\\e\\a\\p\\a\\b\\p\\a\\l\\a\\f\\a\\c\\a\\b\\w\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\p\\a\\b\\e\\a\\l\\a\\d\\a\\p\\a\\b\\l\\a\\d\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\f\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\p\\a\\u\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\p\\a\\G\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\p\\a\\b\\e\\a\\l\\a\\d\\a\\p\\a\\b\\l\\a\\d\\a\\k\\a\\e\\a\\p\\a\\R\\a\\l\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\G\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\k\\a\\x\\a\\F\\a\\l\\a\\d\\a\\e\\a\\Q\\a\\P\\a\\o\\a\\c\\a\\b\\w\\a\\d\\a\\k\\a\\e\\a\\Q\\a\\12\\a\\l\\a\\C\\a\\p\\a\\N\\a\\H\\a\\Q\\a\\y\\a\\Q\\a\\14\\a\\H\\a\\b\\e\\a\\y\\a\\Q\\a\\S\\a\\H\\a\\Q\\a\\b\\m\\a\\y\\a\\p\\a\\A\\a\\H\\a\\p\\a\\b\\X\\a\\y\\a\\Q\\a\\K\\a\\H\\a\\J\\a\\d\\a\\d\\a\\y\\a\\d\\a\\d\\a\\I\\a\\y\\a\\Q\\a\\u\\a\\H\\a\\p\\a\\b\\X\\a\\y\\a\\Q\\a\\t\\a\\H\\a\\p\\a\\b\\X\\a\\y\\a\\Q\\a\\b\\X\\a\\H\\a\\Q\\a\\G\\a\\y\\a\\Q\\a\\R\\a\\H\\a\\Q\\a\\q\\a\\y\\a\\Q\\a\\b\\13\\a\\H\\a\\C\\a\\P\\a\\H\\a\\C\\a\\p\\a\\N\\a\\H\\a\\c\\a\\y\\a\\p\\a\\A\\a\\H\\a\\p\\a\\b\\X\\a\\B\\a\\y\\a\\Q\\a\\11\\a\\H\\a\\C\\a\\p\\a\\N\\a\\H\\a\\p\\a\\y\\a\\p\\a\\A\\a\\H\\a\\p\\a\\b\\X\\a\\B\\a\\y\\a\\Q\\a\\z\\a\\H\\a\\C\\a\\p\\a\\N\\a\\H\\a\\Q\\a\\y\\a\\p\\a\\A\\a\\H\\a\\p\\a\\b\\X\\a\\B\\a\\B\\a\\B\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\e\\a\\c\\a\\G\\a\\o\\a\\p\\a\\b\\i\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\z\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\B\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\B\\a\\k\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\x\\a\\F\\a\\l\\a\\d\\a\\b\\C\\a\\c\\a\\b\\o\\a\\o\\a\\p\\a\\p\\a\\d\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\X\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\p\\a\\b\\f\\a\\l\\a\\k\\a\\x\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\n\\a\\o\\a\\n\\a\\d\\a\\m\\a\\b\\X\\a\\m\\a\\d\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\Q\\a\\d\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\o\\a\\o\\a\\c\\a\\M\\a\\d\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\d\\a\\c\\a\\b\\j\\a\\d\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\w\\a\\g\\a\\11\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\V\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\K\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\k\\a\\J\\a\\P\\a\\I\\a\\e\\a\\c\\a\\b\\y\\a\\x\\a\\w\\a\\g\\a\\R\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\n\\a\\e\\a\\F\\a\\A\\a\\y\\a\\b\\h\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\b\\l\\a\\k\\a\\y\\a\\b\\g\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\e\\a\\y\\a\\b\\i\\a\\k\\a\\y\\a\\b\\13\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\m\\a\\y\\a\\c\\a\\P\\a\\k\\a\\y\\a\\N\\a\\h\\a\\p\\a\\P\\a\\J\\a\\p\\a\\c\\a\\l\\a\\b\\g\\a\\y\\a\\c\\a\\P\\a\\k\\a\\I\\a\\m\\a\\f\\a\\g\\a\\f\\a\\m\\a\\b\\13\\a\\m\\a\\f\\a\\y\\a\\g\\a\\f\\a\\m\\a\\b\\h\\a\\x\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\F\\a\\G\\a\\h\\a\\F\\a\\l\\a\\f\\a\\i\\a\\u\\a\\j\\a\\f\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\G\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\c\\a\\b\\t\\a\\e\\a\\c\\a\\r\\a\\n\\a\\c\\a\\b\\s\\a\\n\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\18\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\c\\a\\F\\a\\c\\a\\b\\U\\a\\e\\a\\19\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\14\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\18\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\i\\a\\b\\o\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\p\\a\\h\\a\\F\\a\\G\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\b\\o\\a\\H\\a\\c\\a\\b\\b\\a\\f\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\U\\a\\f\\a\\k\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\b\\p\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\c\\a\\b\\u\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\c\\a\\A\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\o\\a\\o\\a\\c\\a\\b\\13\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\o\\a\\o\\a\\c\\a\\S\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\o\\a\\o\\a\\b\\w\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\o\\a\\o\\a\\b\\o\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\o\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\b\\o\\a\\o\\a\\b\\j\\a\\d\\a\\j\\a\\i\\a\\b\\b\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\q\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\c\\a\\A\\a\\j\\a\\f\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\s\\a\\d\\a\\n\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\d\\a\\b\\C\\a\\c\\a\\b\\o\\a\\o\\a\\p\\a\\p\\a\\d\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\c\\a\\b\\o\\a\\o\\a\\b\\o\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\z\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\B\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\B\\a\\k\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\k\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\Y\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\w\\a\\g\\a\\p\\a\\G\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\d\\a\\O\\a\\d\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\p\\a\\b\\c\\a\\o\\a\\b\\c\\a\\d\\a\\k\\a\\y\\a\\p\\a\\w\\a\\h\\a\\d\\a\\p\\a\\11\\a\\d\\a\\y\\a\\p\\a\\r\\a\\h\\a\\d\\a\\c\\a\\q\\a\\d\\a\\y\\a\\p\\a\\12\\a\\h\\a\\d\\a\\b\\c\\a\\d\\a\\y\\a\\c\\a\\G\\a\\h\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\d\\a\\O\\a\\d\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\x\\a\\T\\a\\l\\a\\c\\a\\G\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\p\\a\\w\\a\\k\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\d\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\A\\a\\k\\a\\C\\a\\A\\a\\h\\a\\A\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\o\\a\\b\\e\\a\\y\\a\\A\\a\\h\\a\\p\\a\\Q\\a\\e\\a\\p\\a\\18\\a\\l\\a\\p\\a\\Q\\a\\e\\a\\p\\a\\11\\a\\l\\a\\k\\a\\b\\E\\a\\l\\a\\A\\a\\o\\a\\P\\a\\m\\a\\c\\a\\k\\a\\k\\a\\m\\a\\P\\a\\y\\a\\P\\a\\h\\a\\h\\a\\A\\a\\b\\x\\a\\b\\x\\a\\l\\a\\A\\a\\h\\a\\p\\a\\Q\\a\\e\\a\\p\\a\\18\\a\\l\\a\\p\\a\\Q\\a\\e\\a\\p\\a\\11\\a\\l\\a\\k\\a\\b\\E\\a\\l\\a\\A\\a\\o\\a\\P\\a\\m\\a\\c\\a\\k\\a\\k\\a\\m\\a\\c\\a\\k\\a\\y\\a\\A\\a\\h\\a\\h\\a\\P\\a\\b\\x\\a\\b\\x\\a\\l\\a\\A\\a\\h\\a\\h\\a\\c\\a\\k\\a\\y\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\Q\\a\\b\\l\\a\\o\\a\\p\\a\\b\\j\\a\\h\\a\\d\\a\\m\\a\\A\\a\\m\\a\\d\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\b\\e\\a\\d\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\p\\a\\16\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\p\\a\\R\\a\\d\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\d\\a\\c\\a\\b\\j\\a\\d\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\w\\a\\g\\a\\11\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\V\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\K\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\k\\a\\J\\a\\P\\a\\I\\a\\e\\a\\c\\a\\b\\y\\a\\x\\a\\w\\a\\g\\a\\b\\q\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\p\\a\\b\\m\\a\\J\\a\\P\\a\\I\\a\\e\\a\\p\\a\\q\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\R\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\n\\a\\e\\a\\F\\a\\A\\a\\y\\a\\b\\h\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\b\\l\\a\\k\\a\\y\\a\\b\\g\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\e\\a\\y\\a\\b\\i\\a\\k\\a\\y\\a\\b\\13\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\m\\a\\y\\a\\c\\a\\P\\a\\k\\a\\y\\a\\N\\a\\h\\a\\p\\a\\P\\a\\J\\a\\p\\a\\c\\a\\l\\a\\b\\g\\a\\y\\a\\c\\a\\P\\a\\k\\a\\I\\a\\m\\a\\f\\a\\g\\a\\f\\a\\m\\a\\b\\13\\a\\m\\a\\f\\a\\y\\a\\g\\a\\f\\a\\m\\a\\b\\h\\a\\x\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\F\\a\\G\\a\\h\\a\\F\\a\\l\\a\\f\\a\\i\\a\\u\\a\\j\\a\\f\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\G\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\c\\a\\b\\t\\a\\e\\a\\c\\a\\r\\a\\n\\a\\c\\a\\b\\s\\a\\n\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\18\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\c\\a\\F\\a\\c\\a\\b\\U\\a\\e\\a\\19\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\18\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\i\\a\\b\\o\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\p\\a\\h\\a\\F\\a\\G\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\b\\o\\a\\H\\a\\c\\a\\b\\b\\a\\f\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\U\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\b\\p\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\c\\a\\b\\u\\a\\B\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\P\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\c\\a\\b\\v\\a\\g\\a\\c\\a\\u\\a\\o\\a\\p\\a\\b\\d\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\T\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\c\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\O\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\p\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\c\\a\\b\\v\\a\\g\\a\\c\\a\\u\\a\\o\\a\\p\\a\\17\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\M\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\Q\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\c\\a\\b\\v\\a\\g\\a\\c\\a\\u\\a\\o\\a\\p\\a\\b\\h\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\15\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\b\\10\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\Y\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\T\\a\\l\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\d\\a\\O\\a\\d\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\d\\a\\p\\a\\11\\a\\d\\a\\k\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\e\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\z\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\B\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\B\\a\\k\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\c\\a\\G\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\p\\a\\r\\a\\k\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\d\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\t\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\b\\e\\a\\d\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\p\\a\\16\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\p\\a\\R\\a\\d\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\d\\a\\c\\a\\b\\j\\a\\d\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\w\\a\\g\\a\\11\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\V\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\K\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\k\\a\\J\\a\\P\\a\\I\\a\\e\\a\\c\\a\\b\\y\\a\\x\\a\\w\\a\\g\\a\\b\\q\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\p\\a\\b\\m\\a\\J\\a\\P\\a\\I\\a\\e\\a\\p\\a\\q\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\R\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\n\\a\\e\\a\\F\\a\\A\\a\\y\\a\\b\\h\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\b\\l\\a\\k\\a\\y\\a\\b\\g\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\e\\a\\y\\a\\b\\i\\a\\k\\a\\y\\a\\b\\13\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\m\\a\\y\\a\\c\\a\\P\\a\\k\\a\\y\\a\\N\\a\\h\\a\\p\\a\\P\\a\\J\\a\\p\\a\\c\\a\\l\\a\\b\\g\\a\\y\\a\\c\\a\\P\\a\\k\\a\\I\\a\\m\\a\\f\\a\\g\\a\\f\\a\\m\\a\\b\\13\\a\\m\\a\\f\\a\\y\\a\\g\\a\\f\\a\\m\\a\\b\\h\\a\\x\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\F\\a\\G\\a\\h\\a\\F\\a\\l\\a\\f\\a\\i\\a\\u\\a\\j\\a\\f\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\G\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\c\\a\\b\\t\\a\\e\\a\\c\\a\\r\\a\\n\\a\\c\\a\\b\\s\\a\\n\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\18\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\c\\a\\F\\a\\c\\a\\b\\U\\a\\e\\a\\19\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\18\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\i\\a\\b\\o\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\p\\a\\h\\a\\F\\a\\G\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\b\\o\\a\\H\\a\\c\\a\\b\\b\\a\\f\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\U\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\b\\p\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\c\\a\\b\\u\\a\\B\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\P\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\c\\a\\b\\v\\a\\g\\a\\c\\a\\u\\a\\o\\a\\p\\a\\b\\d\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\T\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\c\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\O\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\p\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\c\\a\\b\\v\\a\\g\\a\\c\\a\\u\\a\\o\\a\\p\\a\\17\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\M\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\Q\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\c\\a\\b\\v\\a\\g\\a\\c\\a\\u\\a\\o\\a\\p\\a\\b\\h\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\15\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\b\\10\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\Y\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\T\\a\\l\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\d\\a\\O\\a\\d\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\d\\a\\c\\a\\q\\a\\d\\a\\k\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\e\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\z\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\B\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\B\\a\\k\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\c\\a\\G\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\p\\a\\12\\a\\k\\a\\k\\a\\C\\a\\F\\a\\e\\a\\c\\a\\E\\a\\l\\a\\C\\a\\19\\a\\H\\a\\d\\a\\n\\a\\c\\a\\18\\a\\n\\a\\c\\a\\M\\a\\n\\a\\b\\n\\a\\n\\a\\o\\a\\n\\a\\d\\a\\m\\a\\p\\a\\G\\a\\m\\a\\d\\a\\b\\D\\a\\c\\a\\N\\a\\h\\a\\c\\a\\15\\a\\o\\a\\c\\a\\14\\a\\o\\a\\c\\a\\b\\h\\a\\b\\x\\a\\c\\a\\b\\d\\a\\o\\a\\c\\a\\b\\Z\\a\\h\\a\\b\\e\\a\\d\\a\\y\\a\\c\\a\\17\\a\\H\\a\\f\\a\\c\\a\\Y\\a\\f\\a\\y\\a\\c\\a\\b\\q\\a\\H\\a\\d\\a\\c\\a\\O\\a\\d\\a\\y\\a\\c\\a\\b\\g\\a\\H\\a\\17\\a\\l\\a\\q\\a\\k\\a\\C\\a\\w\\a\\g\\a\\M\\a\\h\\a\\d\\a\\d\\a\\x\\a\\w\\a\\g\\a\\S\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\p\\a\\16\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\p\\a\\R\\a\\d\\a\\j\\a\\f\\a\\x\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\z\\a\\h\\a\\P\\a\\x\\a\\z\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\e\\a\\b\\u\\a\\x\\a\\z\\a\\m\\a\\m\\a\\k\\a\\C\\a\\c\\a\\b\\X\\a\\l\\a\\w\\a\\g\\a\\14\\a\\h\\a\\P\\a\\x\\a\\14\\a\\i\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\e\\a\\b\\u\\a\\x\\a\\14\\a\\m\\a\\m\\a\\k\\a\\C\\a\\T\\a\\l\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\c\\a\\b\\1b\\a\\h\\a\\h\\a\\d\\a\\c\\a\\b\\j\\a\\d\\a\\k\\a\\C\\a\\M\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\1b\\a\\J\\a\\14\\a\\I\\a\\e\\a\\E\\a\\x\\a\\c\\a\\b\\10\\a\\B\\a\\B\\a\\w\\a\\g\\a\\11\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\V\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\K\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\k\\a\\J\\a\\P\\a\\I\\a\\e\\a\\c\\a\\b\\y\\a\\x\\a\\w\\a\\g\\a\\b\\q\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\p\\a\\b\\m\\a\\J\\a\\P\\a\\I\\a\\e\\a\\p\\a\\q\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\R\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\n\\a\\e\\a\\F\\a\\A\\a\\y\\a\\b\\h\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\P\\a\\y\\a\\b\\l\\a\\k\\a\\y\\a\\b\\g\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\e\\a\\y\\a\\b\\i\\a\\k\\a\\y\\a\\b\\13\\a\\h\\a\\R\\a\\e\\a\\b\\k\\a\\l\\a\\b\\m\\a\\y\\a\\c\\a\\P\\a\\k\\a\\y\\a\\N\\a\\h\\a\\p\\a\\P\\a\\J\\a\\p\\a\\c\\a\\l\\a\\b\\g\\a\\y\\a\\c\\a\\P\\a\\k\\a\\I\\a\\m\\a\\f\\a\\g\\a\\f\\a\\m\\a\\b\\13\\a\\m\\a\\f\\a\\y\\a\\g\\a\\f\\a\\m\\a\\b\\h\\a\\x\\a\\w\\a\\g\\a\\G\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\b\\j\\a\\e\\a\\F\\a\\A\\a\\x\\a\\w\\a\\g\\a\\F\\a\\G\\a\\h\\a\\F\\a\\l\\a\\f\\a\\i\\a\\u\\a\\j\\a\\f\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\G\\a\\k\\a\\x\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\c\\a\\b\\t\\a\\e\\a\\c\\a\\r\\a\\n\\a\\c\\a\\b\\s\\a\\n\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\18\\a\\h\\a\\q\\a\\e\\a\\r\\a\\e\\a\\D\\a\\J\\a\\z\\a\\I\\a\\e\\a\\c\\a\\b\\c\\a\\F\\a\\c\\a\\b\\U\\a\\e\\a\\19\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\18\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\G\\a\\e\\a\\c\\a\\11\\a\\l\\a\\d\\a\\i\\a\\b\\o\\a\\d\\a\\k\\a\\j\\a\\o\\a\\c\\a\\k\\a\\C\\a\\w\\a\\g\\a\\b\\p\\a\\h\\a\\F\\a\\G\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\b\\o\\a\\H\\a\\c\\a\\b\\b\\a\\f\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\U\\a\\f\\a\\k\\a\\x\\a\\w\\a\\g\\a\\12\\a\\h\\a\\b\\p\\a\\B\\a\\b\\d\\a\\C\\a\\w\\a\\g\\a\\12\\a\\h\\a\\c\\a\\b\\u\\a\\B\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\P\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\c\\a\\b\\v\\a\\g\\a\\c\\a\\u\\a\\o\\a\\p\\a\\b\\d\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\T\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\c\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\O\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\p\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\c\\a\\b\\v\\a\\g\\a\\c\\a\\u\\a\\o\\a\\p\\a\\17\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\M\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\g\\a\\T\\a\\l\\a\\z\\a\\h\\a\\h\\a\\Q\\a\\k\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\u\\a\\o\\a\\c\\a\\b\\v\\a\\g\\a\\c\\a\\u\\a\\o\\a\\p\\a\\b\\h\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\15\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\b\\d\\a\\C\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\c\\a\\12\\a\\o\\a\\c\\a\\b\\13\\a\\g\\a\\p\\a\\b\\10\\a\\d\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\D\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\d\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\g\\a\\b\\f\\a\\h\\a\\d\\a\\b\\10\\a\\H\\a\\19\\a\\l\\a\\f\\a\\m\\a\\12\\a\\m\\a\\f\\a\\k\\a\\g\\a\\c\\a\\b\\l\\a\\o\\a\\c\\a\\p\\a\\g\\a\\16\\a\\g\\a\\16\\a\\x\\a\\b\\10\\a\\o\\a\\c\\a\\b\\i\\a\\H\\a\\g\\a\\c\\a\\c\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\z\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\n\\a\\c\\a\\b\\m\\a\\n\\a\\b\\c\\a\\n\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\d\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\Z\\a\\o\\a\\c\\a\\S\\a\\d\\a\\j\\a\\f\\a\\m\\a\\K\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\b\\b\\a\\g\\a\\s\\a\\h\\a\\d\\a\\b\\1a\\a\\o\\a\\b\\V\\a\\d\\a\\j\\a\\i\\a\\t\\a\\g\\a\\E\\a\\h\\a\\d\\a\\f\\a\\m\\a\\M\\a\\m\\a\\f\\a\\d\\a\\j\\a\\f\\a\\m\\a\\11\\a\\m\\a\\f\\a\\i\\a\\n\\a\\t\\a\\j\\a\\i\\a\\n\\a\\b\\b\\a\\j\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\c\\a\\w\\a\\d\\a\\j\\a\\i\\a\\O\\a\\g\\a\\s\\a\\h\\a\\d\\a\\Y\\a\\o\\a\\b\\t\\a\\d\\a\\j\\a\\f\\a\\m\\a\\N\\a\\m\\a\\f\\a\\i\\a\\n\\a\\O\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\B\\a\\B\\a\\S\\a\\m\\a\\h\\a\\f\\a\\i\\a\\u\\a\\g\\a\\s\\a\\h\\a\\d\\a\\p\\a\\s\\a\\d\\a\\n\\a\\j\\a\\i\\a\\n\\a\\u\\a\\j\\a\\f\\a\\x\\a\\F\\a\\l\\a\\f\\a\\e\\a\\Y\\a\\g\\a\\e\\a\\c\\a\\K\\a\\g\\a\\e\\a\\b\\s\\a\\o\\a\\b\\j\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\T\\a\\l\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\d\\a\\O\\a\\d\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\d\\a\\c\\a\\19\\a\\d\\a\\k\\a\\e\\a\\c\\a\\b\\p\\a\\l\\a\\d\\a\\b\\c\\a\\d\\a\\k\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\Q\\a\\l\\a\\S\\a\\k\\a\\x\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\c\\a\\b\\e\\a\\l\\a\\f\\a\\e\\a\\b\\1a\\a\\o\\a\\b\\w\\a\\f\\a\\k\\a\\e\\a\\b\\v\\a\\l\\a\\17\\a\\l\\a\\k\\a\\C\\a\\F\\a\\l\\a\\15\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\n\\a\\b\\n\\a\\e\\a\\c\\a\\R\\a\\f\\a\\y\\a\\f\\a\\n\\a\\p\\a\\z\\a\\e\\a\\c\\a\\R\\a\\f\\a\\k\\a\\B\\a\\k\\a\\e\\a\\b\\W\\a\\l\\a\\f\\a\\b\\f\\a\\f\\a\\y\\a\\17\\a\\l\\a\\z\\a\\y\\a\\b\\U\\a\\k\\a\\C\\a\\c\\a\\T\\a\\g\\a\\b\\U\\a\\e\\a\\c\\a\\t\\a\\l\\a\\f\\a\\c\\a\\b\\V\\a\\o\\a\\G\\a\\f\\a\\y\\a\\f\\a\\c\\a\\b\\W\\a\\f\\a\\k\\a\\B\\a\\k\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\B\\a\\B\\a\\k\\a\\x\\a\\p\\a\\b\\V\\a\\e\\a\\Q\\a\\T\\a\\h\\a\\17\\a\\l\\a\\k\\a\\C\\a\\w\\a\\g\\a\\q\\a\\h\\a\\Q\\a\\17\\a\\e\\a\\Q\\a\\15\\a\\l\\a\\d\\a\\Q\\a\\19\\a\\d\\a\\k\\a\\x\\a\\T\\a\\l\\a\\q\\a\\h\\a\\h\\a\\Q\\a\\16\\a\\k\\a\\C\\a\\p\\a\\b\\V\\a\\e\\a\\Q\\a\\b\\10\\a\\e\\a\\E\\a\\h\\a\\d\\a\\p\\a\\b\\13\\a\\H\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\p\\a\\b\\1a\\a\\e\\a\\c\\a\\r\\a\\n\\a\\d\\a\\B\\a\\q\\a\\e\\a\\p\\a\\b\\U\\a\\l\\a\\d\\a\\E\\a\\d\\a\\y\\a\\d\\a\\p\\a\\b\\13\\a\\H\\a\\n\\a\\n\\a\\c\\a\\16\\a\\e\\a\\p\\a\\b\\1a\\a\\e\\a\\c\\a\\r\\a\\n\\a\\d\\a\\k\\a\\x\\a\\q\\a\\e\\a\\p\\a\\b\\U\\a\\l\\a\\d\\a\\Q\\a\\b\\W\\a\\d\\a\\y\\a\\d\\a\\Q\\a\\b\\d\\a\\d\\a\\k\\a\\x\\a\\q\\a\\e\\a\\p\\a\\b\\U\\a\\l\\a\\d\\a\\b\\V\\a\\d\\a\\y\\a\\d\\a\\Q\\a\\b\\f\\a\\g\\a\\Q\\a\\b\\1a\\a\\d\\a\\k\\a\\x\\a\\q\\a\\e\\a\\Q\\a\\b\\V\\a\\h\\a\\d\\a\\Q\\a\\b\\Z\\a\\d\\a\\B\\1h\\1g\\1h\\a\\v\\1h\\1g\\1h\\a\\K\\a\\18\\a\\w\\a\\z\\a\\A\\1h\\1g\\1h\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\G\\a\\w\\a\\t\\a\\K\\a\\K\\a\\v\\a\\v\\a\\v\\a\\R\\a\\z\\a\\b\\h\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\b\\h\\a\\t\\a\\N\\a\\v\\a\\q\\a\\r\\a\\A\\a\\N\\a\\b\\q\\a\\v\\a\\b\\13\\a\\q\\a\\q\\a\\R\\a\\v\\a\\S\\a\\N\\a\\q\\a\\b\\13\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\v\\a\\K\\a\\18\\a\\t\\a\\r\\a\\v\\a\\v\\a\\b\\13\\a\\q\\a\\t\\a\\A\\a\\M\\a\\N\\a\\q\\a\\R\\a\\v\\a\\z\\a\\b\\13\\a\\v\\a\\b\\13\\a\\M\\a\\r\\a\\G\\a\\A\\a\\z\\a\\E\\a\\r\\a\\v\\a\\A\\a\\S\\a\\z\\a\\K\\a\\v\\a\\M\\a\\N\\a\\w\\a\\v\\a\\G\\a\\q\\a\\r\\a\\A\\a\\q\\a\\N\\a\\v\\a\\b\\X\\a\\t\\a\\G\\a\\12\\a\\11\\a\\N\\a\\E\\a\\M\\a\\r\\a\\R\\a\\v\\a\\S\\a\\Q\\a\\v\\a\\K\\a\\N\\a\\G\\a\\v\\a\\t\\a\\A\\a\\A\\a\\N\\a\\v\\a\\q\\a\\w\\a\\K\\a\\q\\a\\v\\a\\K\\a\\A\\a\\b\\q\\a\\w\\a\\q\\a\\v\\a\\N\\a\\G\\a\\18\\a\\v\\a\\A\\a\\z\\a\\A\\a\\w\\a\\q\\a\\v\\a\\18\\a\\E\\a\\K\\a\\A\\a\\v\\a\\w\\a\\z\\a\\r\\a\\12\\a\\v\\a\\G\\a\\E\\a\\r\\a\\A\\a\\q\\a\\r\\a\\A\\a\\v\\a\\z\\a\\D\\a\\11\\a\\v\\a\\K\\a\\M\\a\\b\\X\\a\\K\\a\\A\\a\\N\\a\\z\\a\\r\\a\\11\\a\\v\\a\\v\\a\\w\\a\\t\\a\\b\\X\\a\\q\\a\\w\\a\\v\\a\\R\\a\\q\\a\\b\\13\\a\\t\\a\\M\\a\\w\\a\\A\\a\\v\\a\\w\\a\\q\\a\\r\\a\\11\\a\\A\\a\\S\\a\\v\\a\\b\\g\\a\\z\\a\\R\\a\\11\\a\\q\\a\\A\\a\\v\\a\\q\\a\\t\\a\\G\\a\\S\\a\\v\\a\\R\\a\\t\\a\\A\\a\\q\\a\\v\\a\\A\\a\\S\\a\\M\\a\\D\\a\\b\\X\\a\\v\\a\\v\\a\\G\\a\\E\\a\\b\\h\\a\\q\\a\\N\\a\\v\\a\\N\\a\\q\\a\\18\\a\\q\\a\\t\\a\\A\\a\\v\\a\\S\\a\\A\\a\\D\\a\\w\\a\\v\\a\\r\\a\\E\\a\\v\\a\\b\\13\\a\\z\\a\\r\\a\\R\\a\\v\\a\\E\\a\\b\\h\\a\\q\\a\\N\\a\\w\\a\\t\\a\\b\\q\\a\\v\\a\\K\\a\\z\\a\\Y\\a\\q\\a\\v\\a\\K\\a\\q\\a\\t\\a\\N\\a\\G\\a\\S\\a\\v\\a\\b\\13\\a\\q\\a\\t\\a\\A\\a\\v\\a\\N\\a\\q\\a\\18\\a\\w\\a\\t\\a\\G\\a\\q\\a\\v\\a\\b\\13\\a\\E\\a\\N\\a\\v\\a\\b\\X\\a\\E\\a\\O\\a\\v\\a\\14\\a\\18\\a\\11\\a\\v\\a\\N\\a\\q\\a\\G\\a\\q\\a\\r\\a\\A\\a\\v\\a\\z\\a\\A\\a\\q\\a\\D\\a\\v\\a\\z\\a\\r\\a\\R\\a\\q\\a\\O\\a\\b\\1b\\a\\b\\13\\a\\v\\a\\A\\a\\t\\a\\11\\a\\v\\a\\18\\a\\t\\a\\r\\a\\q\\a\\w\\a\\v\\a\\z\\a\\r\\a\\v\\a\\S\\a\\E\\a\\A\\a\\v\\a\\D\\a\\q\\a\\A\\a\\t\\a\\v\\a\\z\\a\\r\\a\\r\\a\\q\\a\\N\\a\\v\\a\\G\\a\\E\\a\\D\\a\\v\\a\\t\\a\\14\\a\\t\\a\\O\\a\\v\\a\\b\\13\\a\\q\\a\\q\\a\\R\\a\\K\\a\\v\\a\\D\\a\\t\\a\\A\\a\\G\\a\\S\\a\\v\\a\\t\\a\\w\\a\\A\\a\\v\\a\\b\\U\\a\\b\\c\\a\\b\\V\\a\\b\\1a\\a\\v\\a\\w\\a\\z\\a\\v\\a\\18\\a\\E\\a\\K\\a\\A\\a\\K\\a\\v\\a\\K\\a\\G\\a\\N\\a\\z\\a\\18\\a\\A\\a\\v\\a\\K\\a\\M\\a\\G\\a\\G\\a\\q\\a\\K\\a\\K\\a\\v\\a\\14\\a\\K\\a\\E\\a\\r\\a\\18\\a\\v\\a\\R\\a\\t\\a\\A\\a\\t\\a\\b\\c\\a\\b\\q\\a\\18\\a\\q\\a\\v\\a\\11\\a\\q\\a\\A\\a\\v\\a\\N\\a\\q\\a\\A\\a\\M\\a\\N\\a\\r\\a\\v\\a\\A\\a\\b\\q\\a\\18\\a\\q\\a\\v\\a\\14\\a\\K\\a\\E\\a\\r\\a\\v\\a\\z\\a\\R\\a\\v\\a\\b\\g\\a\\b\\g\\a\\b\\g\\a\\v\\a\\b\\X\\a\\N\\a\\q\\a\\t\\a\\12\\a\\v\\a\\b\\13\\a\\z\\a\\N\\a\\K\\a\\A\\a\\v\\a\\A\\a\\S\\a\\M\\a\\D\\a\\b\\X\\a\\r\\a\\t\\a\\z\\a\\w\\a\\v\\a\\K\\a\\c\\a\\s\\a\\P\\a\\P\\a\\v\\a\\D\\a\\t\\a\\O\\a\\v\\a\\18\\a\\t\\a\\N\\a\\q\\a\\r\\a\\A\\a\\v\\a\\M\\a\\w\\a\\v\\a\\K\\a\\b\\i\\a\\p\\a\\v\\a\\N\\a\\q\\a\\K\\a\\M\\a\\w\\a\\A\\a\\K\\a\\v\\a\\N\\a\\q\\a\\w\\a\\v\\a\\t\\a\\w\\a\\A\\a\\q\\a\\N\\a\\r\\a\\t\\a\\A\\a\\q\\a\\v\\a\\N\\a\\q\\a\\w\\a\\t\\a\\A\\a\\q\\a\\R\\a\\v\\a\\G\\a\\t\\a\\A\\a\\q\\a\\11\\a\\E\\a\\N\\a\\b\\q\\a\\v\\a\\A\\a\\q\\a\\N\\a\\D\\a\\v\\a\\D\\a\\q\\a\\R\\a\\z\\a\\t\\a\\v\\a\\18\\a\\M\\a\\b\\X\\a\\w\\a\\z\\a\\K\\a\\S\\a\\q\\a\\R\\a\\v\\a\\b\\Z\\a\\b\\1b\\a\\b\\r\\a\\b\\W\\a\\b\\V\\a\\T\\a\\b\\b\\a\\16\\a\\v\\a\\q\\a\\D\\a\\b\\X\\a\\q\\a\\R\\a\\v\\a\\t\\a\\w\\a\\z\\a\\11\\a\\r\\a\\v\\a\\b\\q\\a\\E\\a\\M\\a\\A\\a\\M\\a\\b\\X\\a\\q\\a\\v\\a\\G\\a\\t\\a\\N\\a\\E\\a\\M\\a\\K\\a\\q\\a\\w\\a\\v\\a\\b\\V\\a\\b\\1b\\a\\b\\Z\\a\\b\\c\\a\\b\\U\\a\\b\\r\\a\\b\\10\\a\\b\\1b\\a\\b\\k\\a\\b\\V\\a\\T\\a\\b\\c\\a\\v\\a\\18\\a\\t\\a\\N\\a\\K\\a\\q\\a\\b\\W\\a\\r\\a\\A\\a\\v\\a\\N\\a\\q\\a\\t\\a\\R\\a\\b\\q\\a\\v\\a\\b\\V\\a\\t\\a\\A\\a\\S\\a\\v\\a\\S\\a\\p\\a\\v\\a\\18\\a\\N\\a\\q\\a\\b\\h\\a\\v\\a\\G\\a\\w\\a\\q\\a\\t\\a\\N\\a\\v\\a\\z\\a\\D\\a\\t\\a\\11\\a\\q\\a\\v\\a\\t\\a\\M\\a\\A\\a\\S\\a\\E\\a\\N\\a\\v\\a\\b\\X\\a\\w\\a\\v\\a\\b\\X\\a\\t\\a\\K\\a\\q\\a\\v\\a\\A\\a\\N\\a\\M\\a\\q\\a\\v\\a\\b\\X\\a\\A\\a\\v\\a\\b\\g\\a\\N\\a\\t\\a\\18\\a\\v\\a\\r\\a\\t\\a\\D\\a\\q\\a\\v\\a\\S\\a\\A\\a\\A\\a\\18\\a\\v\\a\\N\\a\\t\\a\\r\\a\\R\\a\\E\\a\\D\\a\\v\\a\\b\\X\\a\\E\\a\\O\\a\\q\\a\\K\\a\\v\\a\\S\\a\\b\\p\\a\\R\\a\\q\\a\\b\\13\\a\\t\\a\\M\\a\\w\\a\\A\\a\\v\\a\\D\\a\\b\\p\\a\\R\\a\\q\\a\\b\\13\\a\\t\\a\\M\\a\\w\\a\\A\\a\\v\\a\\b\\X\\a\\Q\\a\\v\\a\\b\\X\\a\\c\\a\\v\\a\\b\\q\\a\\12\\a\\v\\a\\b\\X\\a\\p\\a\\v\\a\\b\\h\\a\\z\\a\\R\\a\\q\\a\\E\\a\\K\\a\\v\\a\\b\\13\\a\\w\\a\\E\\a\\E\\a\\N\\a\\v\\a\\t\\a\\R\\a\\R\\a\\15\\a\\w\\a\\t\\a\\K\\a\\K\\a\\v\\a\\z\\a\\A\\a\\q\\a\\D\\a\\K\\a\\v\\a\\K\\a\\E\\a\\N\\a\\t\\a\\v\\a\\r\\a\\t\\a\\b\\h\\a\\v\\a\\z\\a\\A\\a\\q\\a\\D\\a\\c\\a\\v\\a\\G\\a\\E\\a\\w\\a\\M\\a\\D\\a\\r\\a\\b\\l\\a\\v\\a\\b\\X\\a\\b\\13\\a\\v\\a\\z\\a\\A\\a\\q\\a\\D\\a\\Q\\a\\v\\a\\N\\a\\q\\a\\G\\a\\q\\a\\r\\a\\A\\a\\G\\a\\E\\a\\D\\a\\D\\a\\q\\a\\r\\a\\A\\a\\K\\a\\v\\a\\N\\a\\q\\a\\G\\a\\q\\a\\r\\a\\A\\a\\18\\a\\E\\a\\K\\a\\A\\a\\K\\a\\v\\a\\z\\a\\A\\a\\q\\a\\D\\a\\p\\a\\v\\a\\G\\a\\E\\a\\w\\a\\M\\a\\D\\a\\r\\a\\c\\a\\v\\a\\z\\a\\A\\a\\q\\a\\D\\a\\b\\l\\a\\v\\a\\G\\a\\D\\a\\D\\a\\v\\a\\G\\a\\t\\a\\K\\a\\K\\a\\v\\a\\z\\a\\A\\a\\q\\a\\D\\a\\b\\e\\a\\v\\a\\t\\a\\b\\h\\a\\t\\a\\A\\a\\t\\a\\N\\a\\v\\a\\K\\a\\q\\a\\A\\a\\T\\a\\A\\a\\A\\a\\N\\a\\z\\a\\b\\X\\a\\M\\a\\A\\a\\q\\a\\v\\a\\N\\a\\t\\a\\r\\a\\R\\a\\E\\a\\D\\a\\18\\a\\E\\a\\K\\a\\A\\a\\K\\a\\v\\a\\G\\a\\E\\a\\w\\a\\M\\a\\D\\a\\r\\a\\p\\a\\v\\a\\A\\a\\q\\a\\O\\a\\A\\a\\v\\a\\A\\a\\S\\a\\q\\a\\D\\a\\q\\a\\O\\a\\18\\a\\E\\a\\K\\a\\q\\a\\v\\a\\b\\g\\a\\z\\a\\r\\a\\R\\a\\E\\a\\b\\g\\a\\v\\a\\b\\X\\a\\O\\a\\v\\a\\18\\a\\r\\a\\11\\a\\v\\a\\z\\a\\r\\a\\R\\a\\q\\a\\O\\a\\v\\a\\N\\a\\G\\a\\A\\a\\S\\a\\M\\a\\D\\a\\b\\X\\a\\v\\a\\K\\a\\b\\e\\a\\b\\e\\a\\v\\a\\b\\f\\a\\G\\a\\M\\a\\u\\a\\b\\g\\a\\b\\d\\a\\b\\X\\a\\b\\h\\a\\b\\i\\a\\u\\a\\P\\a\\S\\a\\b\\W\\a\\E\\a\\b\\m\\a\\Q\\a\\N\\a\\b\\W\\a\\b\\r\\a\\K\\a\\b\\i\\a\\w\\a\\b\\1a\\a\\b\\s\\a\\Q\\a\\Y\\a\\12\\a\\b\\1a\\a\\b\\t\\a\\P\\a\\c\\a\\16\\a\\T\\a\\v\\a\\R\\a\\t\\a\\A\\a\\t\\a\\v\\a\\T\\a\\T\\a\\T\\a\\T\\a\\T\\a\\T\\a\\T\\a\\T\\a\\19\\a\\b\\n\\a\\K\\a\\v\\a\\D\\a\\b\\1a\\a\\b\\i\\a\\b\\j\\a\\b\\W\\a\\v\\a\\b\\u\\a\\M\\a\\b\\1b\\a\\b\\1a\\a\\r\\a\\v\\a\\M\\a\\15\\a\\14\\a\\b\\t\\a\\11\\a\\b\\u\\a\\b\\10\\a\\b\\W\\a\\S\\a\\b\\i\\a\\P\\a\\v\\a\\K\\a\\M\\a\\D\\a\\D\\a\\t\\a\\N\\a\\b\\q\\a\\v\\a\\b\\X\\a\\w\\a\\E\\a\\11\\a\\K\\a\\18\\a\\E\\a\\A\\a\\v\\a\\D\\a\\t\\a\\z\\a\\r\\a\\v\\a\\N\\a\\q\\a\\v\\a\\b\\X\\a\\18\\a\\v\\a\\11\\a\\z\\a\\b\\13\\a\\v\\a\\K\\a\\A\\a\\t\\a\\N\\a\\A\\a\\v\\a\\b\\X\\a\\w\\a\\E\\a\\11\\a\\b\\X\\a\\w\\a\\E\\a\\11\\a\\v\\a\\G\\a\\M\\a\\K\\a\\A\\a\\E\\a\\D\\a\\v\\a\\b\\i\\a\\P\\a\\v\\a\\b\\e\\a\\b\\e\\a\\P\\a\\v\\a\\w\\a\\E\\a\\E\\a\\18\\a\\v\\a\\t\\a\\M\\a\\A\\a\\E\\a\\18\\a\\w\\a\\t\\a\\b\\q\\a\\v\\a\\t\\a\\M\\a\\A\\a\\E\\a\\18\\a\\w\\a\\t\\a\\b\\q\\a\\b\\y\\a\\18\\a\\q\\a\\q\\a\\R\\a\\v\\a\\b\\m\\a\\P\\a\\P\\a\\v\\a\\R\\a\\E\\a\\A\\a\\K\\a\\v\\a\\b\\13\\a\\t\\a\\w\\a\\K\\a\\q\\a\\v\\a\\N\\a\\q\\a\\K\\a\\18\\a\\E\\a\\r\\a\\K\\a\\z\\a\\b\\h\\a\\q\\a\\v\\a\\s\\a\\P\\a\\c\\a\\v\\a\\K\\a\\D\\a\\t\\a\\N\\a\\A\\a\\b\\y\\a\\18\\a\\q\\a\\q\\a\\R\\a\\v\\a\\b\\i\\a\\P\\a\\c\\a\\v\\a\\D\\a\\t\\a\\N\\a\\11\\a\\z\\a\\r\\a\\v\\a\\E\\a\\b\\g\\a\\w\\a\\15\\a\\t\\a\\N\\a\\E\\a\\M\\a\\K\\a\\q\\a\\w\\a\\v\\a\\b\\X\\a\\b\\r\\a\\N\\a\\G\\a\\v\\a\\15\\a\\T\\a\\b\\k\\a\\b\\1b\\a\\b\\n\\a\\b\\y\\a\\16\\a\\b\\1a\\a\\b\\r\\a\\b\\Z\\a\\b\\n\\a\\b\\V\\a\\v\\a\\b\\u\\a\\b\\W\\a\\19\\a\\16\\a\\b\\1b\\a\\b\\y\\a\\b\\r\\a\\b\\Z\\a\\b\\n\\a\\b\\V\\a\\v\\a\\b\\13\\a\\b\\X\\a\\E\\a\\O\\a\\v\\a\\b\\s\\a\\b\\W\\a\\19\\a\\b\\b\\a\\16\\a\\b\\c\\a\\b\\r\\a\\b\\k\\a\\16\\a\\15\\a\\16\\a\\b\\Z\\a\\b\\c\\a\\b\\r\\a\\15\\a\\b\\1b\\a\\b\\V\\a\\b\\V\\a\\16\\a\\b\\Z\\a\\b\\c\\a\\b\\r\\a\\b\\Z\\a\\b\\n\\a\\b\\V\\a\\v\\a\\b\\s\\a\\b\\W\\a\\19\\a\\b\\b\\a\\16\\a\\b\\c\\a\\b\\r\\a\\b\\k\\a\\T\\a\\b\\Z\\a\\19\\a\\b\\1b\\a\\b\\V\\a\\b\\r\\a\\b\\j\\a\\b\\1b\\a\\b\\y\\a\\b\\c\\a\\b\\r\\a\\b\\Z\\a\\b\\n\\a\\b\\V\\a\\v\\a\\G\\a\\E\\a\\D\\a\\D\\a\\q\\a\\r\\a\\A\\a\\K\\a\\v\\a\\r\\a\\t\\a\\b\\h\\a\\b\\c\\a\\q\\a\\O\\a\\A\\a\\v\\a\\b\\e\\a\\P\\a\\v\\a\\17\\a\\b\\1b\\a\\b\\v\\a\\b\\r\\a\\b\\Z\\a\\b\\n\\a\\b\\V\\a\\v\\a\\11\\a\\R\\a\\v\\a\\b\\s\\a\\b\\W\\a\\19\\a\\b\\b\\a\\16\\a\\b\\c\\a\\b\\r\\a\\b\\k\\a\\16\\a\\15\\a\\16\\a\\b\\Z\\a\\b\\c\\a\\b\\r\\a\\b\\j\\a\\b\\1b\\a\\b\\y\\a\\b\\c\\a\\b\\r\\a\\b\\Z\\a\\b\\n\\a\\b\\V\\a\\v\\a\\z\\a\\D\\a\\11\\a\\c\\a\\v\\a\\b\\X\\a\\w\\a\\t\\a\\r\\a\\12\\a\\v\\a\\z\\a\\D\\a\\11\\a\\p\\a\\v\\a\\E\\a\\r\\a\\w\\a\\E\\a\\t\\a\\R\\a\\v\\a\\R\\a\\E\\a\\G\\a\\M\\a\\D\\a\\q\\a\\r\\a\\A\\a\\v\\a\\11\\a\\q\\a\\A\\a\\16\\a\\w\\a\\q\\a\\D\\a\\q\\a\\r\\a\\A\\a\\17\\a\\b\\q\\a\\b\\W\\a\\R\\a\\v\\a\\D\\a\\b\\q\\a\\G\\a\\E\\a\\r\\a\\A\\a\\q\\a\\r\\a\\A\\a\\v\\a\\r\\a\\M\\a\\w\\a\\w\\a\\v\\a\\w\\a\\E\\a\\G\\a\\t\\a\\A\\a\\z\\a\\E\\a\\r\\a\\v\\a\\b\\X\\a\\c\\a\\s\\a\\v\\a\\N\\a\\E\\a\\M\\a\\r\\a\\R\\a\\q\\a\\R\\a\\v\\a\\N\\a\\q\\a\\b\\13\\a\\v\\a\\R\\a\\E\\a\\b\\13\\a\\E\\a\\w\\a\\w\\a\\E\\a\\b\\g\\a\\v\\a\\17\\a\\w\\a\\E\\a\\11\\a\\11\\a\\q\\a\\N\\a\\v\\a\\b\\c\\a\\q\\a\\D\\a\\18\\a\\w\\a\\t\\a\\A\\a\\q\\a\\K\\a\\v\\a\\z\\a\\r\\a\\r\\a\\q\\a\\N\\a\\b\\U\\a\\b\\c\\a\\b\\V\\a\\b\\1a\\a\\v\\a\\b\\c\\a\\S\\a\\q\\a\\D\\a\\q\\a\\b\\v\\a\\18\\a\\E\\a\\K\\a\\q\\1h\\1g\\1h\\1h\\1g\\1h\\a\\b\\13\\a\\N\\a\\E\\a\\D\\a\\15\\a\\S\\a\\t\\a\\N\\a\\15\\a\\E\\a\\R\\a\\q\\1h\\1g\\1h\\a\\N\\a\\q\\a\\18\\a\\w\\a\\t\\a\\G\\a\\q\\1h\\1g\\1h\\a\\b\\M\\a\\b\\g\\a\\m\\1h\\1g\\1h\\a\\b\\M\\a\\b\\X\\1h\\1g\\1h\\a\\11\\1h\\1d\\1o\\b\\Y\\1e\\b\\J\\1e\\b\\I\\1g\\b\\G\\1g\\b\\z\\1g\\b\\F\\1g\\b\\B\\1g\\b\\K\\1f\\1l\\b\\B\\1n\\b\\J\\1e\\b\\z\\1f\\1l\\b\\H\\1e\\b\\z\\1O\\b\\G\\1A\\b\\A\\1c\\10\\1d\\1B\\b\\B\\1e\\b\\11\\1e\\b\\z\\1y\\b\\G\\1f\\1f\\1f\\1r\\1e\\1e\\b\\z\\1n\\b\\z\\1P\\b\\G\\1f\\1S\\b\\12\\1A\\b\\N\\1c\\b\\A\\1c\\X\\1d\\1d\\1e\\b\\z\\1r\\b\\R\\1f\\1B\\b\\z\\1F\\b\\Q\\1e\\b\\S\\1f\\1f\\1m\\1o\\b\\O\\1e\\1M\\b\\A\\1c\\10\\1d\\1c\\b\\A\\1c\\Z\\1d\\1d\\1e\\1y\\1N\\1y\\1g\\b\\N\\1f\\1f\\1l\\b\\P\\1e\\b\\z\\1v\\1v\\1f\\1l\\b\\K\\1c\\b\\B\\1e\\b\\z\\1f\\1d\\1n\\b\\F\\1c\\b\\z\\1d\\L\\L\\b\\B\\1e\\b\\z\\1f\\1m\\1o\\b\\F\\1n\\1c\\b\\J\\1e\\b\\B\\1f\\1l\\b\\H\\1s\\b\\K\\1c\\b\\B\\1d\\1m\\1d\\1o\\b\\B\\1n\\b\\J\\1e\\1f\\1l\\b\\H\\1s\\b\\A\\1c\\U\\1d\\1m\\1o\\b\\z\\1n\\b\\1m\\1o\\b\\P\\1e\\b\\z\\1v\\1v\\1f\\1l\\b\\O\\1e\\b\\F\\1c\\b\\z\\1d\\1f\\1l\\b\\I\\1n\\b\\I\\1c\\b\\A\\1c\\Z\\1d\\1d\\1e\\b\\14\\1s\\b\\15\\1e\\b\\A\\1c\\1a\\1d\\1r\\b\\B\\1e\\b\\z\\1f\\1r\\b\\A\\1c\\1a\\1d\\1g\\b\\A\\1c\\1b\\1d\\1f\\1g\\b\\F\\1c\\b\\z\\1d\\1f\\1m\\1m\\1o\\b\\H\\1s\\b\\I\\1m\\1e\\b\\A\\1c\\13\\1d\\1g\\b\\17\\1g\\b\\18\\1g\\b\\A\\1c\\V\\1d\\1c\\b\\A\\1c\\W\\1d\\1d\\1e\\b\\A\\1c\\b\\1d\\1f\\1g\\13\\1g\\1l\\1m\\1f\\1f","\\L","\\v\\s\\m\\k\\w","\\L\\L\\L\\L\\L\\L\\L\\L\\L\\L\\r\\V\\b\\L\\r\\W\\W\\L\\r\\W\\G\\L\\r\\W\\U\\L\\r\\W\\13\\L\\r\\V\\F\\L\\r\\V\\E\\L\\r\\V\\G\\L\\r\\W\\1b\\L\\r\\W\\1a\\L\\r\\W\\H\\L\\r\\W\\C\\L\\r\\W\\F\\L\\r\\V\\W\\L\\r\\Z\\X\\L\\r\\V\\Z\\L\\r\\V\\1b\\L\\r\\Z\\b\\L\\r\\U\\E\\L\\r\\Z\\E\\L\\r\\V\\C\\L\\r\\W\\E\\L\\r\\Z\\1b\\L\\r\\Z\\G\\L\\r\\U\\10\\L\\r\\Z\\F\\L\\r\\U\\F\\L\\r\\U\\C\\L\\r\\Z\\H\\L\\r\\W\\10\\L\\r\\Z\\V\\L\\r\\V\\B\\L\\r\\X\\C\\L\\r\\X\\F\\L\\r\\U\\V\\L\\r\\U\\X\\L\\r\\U\\W\\L\\r\\U\\1a\\L\\r\\V\\13\\L\\r\\Z\\10\\L\\r\\V\\V\\L\\r\\Z\\1a\\L\\r\\10\\b\\L\\r\\U\\B\\L\\r\\Z\\U\\L\\r\\Z\\C\\L\\r\\Z\\B\\L\\r\\10\\V\\L\\r\\10\\X\\L\\r\\10\\W\\L\\r\\U\\13\\L\\r\\10\\10\\L\\r\\Z\\Z\\L\\r\\10\\U\\L\\r\\10\\1b\\L\\r\\10\\F\\L\\r\\10\\Z\\L\\r\\Z\\W\\L\\r\\10\\G\\L\\r\\10\\1a\\L\\r\\10\\E\\L\\r\\10\\H\\L\\r\\X\\10\\L\\r\\10\\B\\L\\r\\V\\X\\L\\r\\10\\C\\L\\r\\U\\U\\L\\r\\U\\Z\\L\\r\\V\\U\\L\\r\\X\\13\\L\\r\\X\\W\\L\\r\\V\\10\\L\\r\\X\\X\\L\\r\\V\\1a\\L\\r\\X\\b\\L\\r\\U\\b\\L\\r\\U\\1b\\L\\r\\X\\U\\L\\r\\X\\Z\\L\\r\\X\\1b\\L\\r\\X\\1a\\L\\r\\X\\B\\L\\r\\W\\Z\\L\\r\\X\\V\\L\\1p\\13\\r\\e\\e\\U\\U\\r\\V\\L\\r\\X\\H\\L\\1p\\13\\r\\d\\X\\Z\\Z\\L\\r\\V\\H\\L\\1p\\13\\r\\e\\e\\U\\U\\r\\X\\L\\r\\W\\V\\L\\r\\W\\B\\L\\1p\\13\\r\\e\\e\\U\\U\\r\\10\\L\\1p\\13\\r\\e\\e\\U\\U\\r\\W\\L\\t\\g\\w\\x\\t\\p\\L\\h\\x\\p\\e\\w\\k\\q\\p\\L\\1p\\13\\r\\e\\e\\U\\U\\r\\b\\L\\1p\\13\\r\\e\\e\\U\\U\\r\\Z\\L\\r\\X\\E\\L\\11\\w\\t\\k\\p\\i\\L\\k\\h\\L\\z\\j\\k\\m\\g\\L\\W\\1b\\L\\w\\q\\11\\w\\t\\k\\p\\i\\L\\V\\Z\\L\\r\\X\\G\\L\\g\\y\\c\\m\\L\\s\\c\\t\\v\\g\\K\\p\\w\\L\\V\\X\\L\\p\\g\\z\\L\\Y\\g\\i\\G\\r\\s\\L\\y\\c\\t\\L\\Z\\W\\L\\W\\V\\Z","","\\h\\t\\q\\o\\E\\j\\c\\t\\E\\q\\f\\g","\\t\\g\\s\\m\\c\\e\\g","\\a\\z\\1r","\\a\\d","\\i"];1T(1w(1x,1u,1i,1q,1k,1z){1k=1w(1i){1t(1i<1u?1j[4]:1k(1G(1i/1u)))+((1i=1i%1u)>1H?1C[1j[5]](1i+1J):1i.1K(1L))};1D(!1j[4][1j[6]](/^/,1C)){1E(1i--){1z[1k(1i)]=1q[1i]||1k(1i)};1q=[1w(1k){1t 1z[1k]}];1k=1w(){1t 1j[7]};1i=1};1E(1i--){1D(1q[1i]){1x=1x[1j[6]](1Q 1R(1j[8]+1k(1i)+1j[8],1j[9]),1q[1i])}};1t 1x}(1j[0],1U,1V,1j[3][1j[2]](1j[1]),0,{}))',62,120,'||||||||||x5C|x31|x61|x62|x63|x64|x65|x66|x67|x68|x69|x6A|x6C|x6B|x6D|x6E|x6F|x78|x70|x72|x71|x73|x74|x75|x76|x77|x79|x41|x42|x7A|x43|x44|x45|x46|x48|x47|x49|x7C|x4A|x4B|x4C|x4D|x4F|x4E|x50|x51|x37|x33|x32|x35|x52|x36|x34|x53|x54|x30|x55|x56|x57|x58|x59|x5A|x38|x39|x5B|x5D|x28|x29|x2C|x22|_0xb9c4x3|_0xe1eb|_0xb9c4x5|x7B|x7D|x3D|x3B|x5F|_0xb9c4x4|x2B|x20|return|_0xb9c4x2|x2D|function|_0xb9c4x1|x2F|_0xb9c4x6|x3F|x3A|String|if|while|x2E|parseInt|35|var|29|toString|36|x21|x5E|x3C|x25|new|RegExp|x3E|eval|62|123'.split('|'),0,{}))

//]]>
</script>

<script type='text/javascript'>
var postperpage=POSTPERPAGE_NUM;
var numshowpage=3;
var upPageWord=&#39;&lt;i class=&quot;fa fa-angle-double-left&quot;&gt;&lt;/i&gt;&#39;;
var downPageWord=&#39;&lt;i class=&quot;fa fa-angle-double-right&quot;&gt;&lt;/i&gt;&#39;;
var urlactivepage=location.href;
var home_page=&quot;/&quot;;
</script>
<b:if cond='data:blog.pageType != &quot;item&quot;'>
<script>
//<![CDATA[
var nopage;var jenis;var nomerhal;var lblname1;halamanblogger();function loophalaman(banyakdata){var html='';nomerkiri=parseInt(numshowpage/2);if(nomerkiri==numshowpage-nomerkiri){numshowpage=nomerkiri*2+1}mulai=nomerhal-nomerkiri;if(mulai<1)mulai=1;maksimal=parseInt(banyakdata/postperpage)+1;if(maksimal-1==banyakdata/postperpage)maksimal=maksimal-1;akhir=mulai+numshowpage-1;if(akhir>maksimal)akhir=maksimal;html+="<span class='showpageOf'>Page "+nomerhal+' of '+maksimal+"</span>";var prevnomer=parseInt(nomerhal)-1;if(nomerhal>1){if(nomerhal==2){if(jenis=="page"){html+='<span class="showpage"><a href="'+home_page+'">'+upPageWord+'</a></span>'}else{html+='<span class="showpageNum"><a href="/search/label/'+lblname1+'?&max-results='+postperpage+'">'+upPageWord+'</a></span>'}}else{if(jenis=="page"){html+='<span class="showpageNum"><a href="#" onclick="redirectpage('+prevnomer+');return false">'+upPageWord+'</a></span>'}else{html+='<span class="showpageNum"><a href="#" onclick="redirectlabel('+prevnomer+');return false">'+upPageWord+'</a></span>'}}}if(mulai>1){if(jenis=="page"){html+='<span class="showpageNum"><a href="'+home_page+'">1</a></span>'}else{html+='<span class="showpageNum"><a href="/search/label/'+lblname1+'?&max-results='+postperpage+'">1</a></span>'}}if(mulai>2){html+='  '}for(var jj=mulai;jj<=akhir;jj++){if(nomerhal==jj){html+='<span class="showpagePoint">'+jj+'</span>'}else if(jj==1){if(jenis=="page"){html+='<span class="showpageNum"><a href="'+home_page+'">1</a></span>'}else{html+='<span class="showpageNum"><a href="/search/label/'+lblname1+'?&max-results='+postperpage+'">1</a></span>'}}else{if(jenis=="page"){html+='<span class="showpageNum"><a href="#" onclick="redirectpage('+jj+');return false">'+jj+'</a></span>'}else{html+='<span class="showpageNum"><a href="#" onclick="redirectlabel('+jj+');return false">'+jj+'</a></span>'}}}if(akhir<maksimal-1){html+=''}if(akhir<maksimal){if(jenis=="page"){html+='<span class="showpageNum"><a href="#" onclick="redirectpage('+maksimal+');return false">'+maksimal+'</a></span>'}else{html+='<span class="showpageNum"><a href="#" onclick="redirectlabel('+maksimal+');return false">'+maksimal+'</a></span>'}}var nextnomer=parseInt(nomerhal)+1;if(nomerhal<maksimal){if(jenis=="page"){html+='<span class="showpageNum"><a href="#" onclick="redirectpage('+nextnomer+');return false">'+downPageWord+'</a></span>'}else{html+='<span class="showpageNum"><a href="#" onclick="redirectlabel('+nextnomer+');return false">'+downPageWord+'</a></span>'}}var pageArea=document.getElementsByName("pageArea");var blogPager=document.getElementById("blog-pager");for(var p=0;p<pageArea.length;p++){pageArea[p].innerHTML=html}if(pageArea&&pageArea.length>0){html=''}if(blogPager){blogPager.innerHTML=html}}function hitungtotaldata(root){var feed=root.feed;var totaldata=parseInt(feed.openSearch$totalResults.$t,10);loophalaman(totaldata)}function halamanblogger(){var thisUrl=urlactivepage;if(thisUrl.indexOf("/search/label/")!=-1){if(thisUrl.indexOf("?updated-max")!=-1){lblname1=thisUrl.substring(thisUrl.indexOf("/search/label/")+14,thisUrl.indexOf("?updated-max"))}else{lblname1=thisUrl.substring(thisUrl.indexOf("/search/label/")+14,thisUrl.indexOf("?&max"))}}if(thisUrl.indexOf("?q=")==-1&&thisUrl.indexOf(".html")==-1){if(thisUrl.indexOf("/search/label/")==-1){jenis="page";if(urlactivepage.indexOf("#PageNo=")!=-1){nomerhal=urlactivepage.substring(urlactivepage.indexOf("#PageNo=")+8,urlactivepage.length)}else{nomerhal=1}document.write("<script src=\""+home_page+"feeds/posts/summary?max-results=1&alt=json-in-script&callback=hitungtotaldata\"><\/script>")}else{jenis="label";if(thisUrl.indexOf("&max-results=")==-1){postperpage=20}if(urlactivepage.indexOf("#PageNo=")!=-1){nomerhal=urlactivepage.substring(urlactivepage.indexOf("#PageNo=")+8,urlactivepage.length)}else{nomerhal=1}document.write('<script src="'+home_page+'feeds/posts/summary/-/'+lblname1+'?alt=json-in-script&callback=hitungtotaldata&max-results=1" ><\/script>')}}}function redirectpage(numberpage){jsonstart=(numberpage-1)*postperpage;nopage=numberpage;var nBody=document.getElementsByTagName('head')[0];var newInclude=document.createElement('script');newInclude.type='text/javascript';newInclude.setAttribute("src",home_page+"feeds/posts/summary?start-index="+jsonstart+"&max-results=1&alt=json-in-script&callback=finddatepost");nBody.appendChild(newInclude)}function redirectlabel(numberpage){jsonstart=(numberpage-1)*postperpage;nopage=numberpage;var nBody=document.getElementsByTagName('head')[0];var newInclude=document.createElement('script');newInclude.type='text/javascript';newInclude.setAttribute("src",home_page+"feeds/posts/summary/-/"+lblname1+"?start-index="+jsonstart+"&max-results=1&alt=json-in-script&callback=finddatepost");nBody.appendChild(newInclude)}function finddatepost(root){post=root.feed.entry[0];var timestamp1=post.published.$t.substring(0,19)+post.published.$t.substring(23,29);var timestamp=encodeURIComponent(timestamp1);if(jenis=="page"){var alamat="/search?updated-max="+timestamp+"&max-results="+postperpage+"#PageNo="+nopage}else{var alamat="/search/label/"+lblname1+"?updated-max="+timestamp+"&max-results="+postperpage+"#PageNo="+nopage}location.href=alamat}
//]]>
</script>
</b:if>
<script>
//<![CDATA[
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.5";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
//]]>
</script>
</body>
</html>