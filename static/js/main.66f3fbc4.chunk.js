(this["webpackJsonpmain-ui"]=this["webpackJsonpmain-ui"]||[]).push([[0],{11:function(e,t,a){},13:function(e,t,a){},15:function(e,t,a){"use strict";a.r(t);var c=a(1),s=a.n(c),n=a(6),r=a.n(n),j=(a(11),a(3)),b=a.n(j),o=a(4),i=a(2),l=a.p+"static/media/logo.6ce24c58.svg",u=(a(13),a(0));var O=function(){var e=Object(c.useState)(),t=Object(i.a)(e,2),a=(t[0],t[1]),s=Object(c.useState)("\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d"),n=Object(i.a)(s,2),r=(n[0],n[1],Object(c.useState)(l)),j=Object(i.a)(r,2),O=j[0],p=j[1],h=Object(c.useState)(l),x=Object(i.a)(h,2),d=x[0],m=x[1],g=Object(c.useState)(!1),f=Object(i.a)(g,2),v=f[0],S=f[1],y=Object(c.useState)(!1),C=Object(i.a)(y,2),N=C[0],A=C[1],k=Object(c.useState)(""),w=Object(i.a)(k,2),L=w[0],T=w[1],_=Object(c.useState)(""),E=Object(i.a)(_,2),F=E[0],D=E[1],J=Object(c.useState)(""),B=Object(i.a)(J,2),P=B[0],I=B[1],R=Object(c.useState)(""),X=Object(i.a)(R,2),G=X[0],M=X[1],U=Object(c.useState)(""),q=Object(i.a)(U,2),z=q[0],H=q[1],K=Object(c.useState)(""),Q=Object(i.a)(K,2),V=(Q[0],Q[1],Object(c.useState)("")),W=Object(i.a)(V,2),Y=(W[0],W[1],Object(c.useState)("")),Z=Object(i.a)(Y,2),$=(Z[0],Z[1],Object(c.useState)("")),ee=Object(i.a)($,2),te=(ee[0],ee[1],Object(c.useState)("")),ae=Object(i.a)(te,2),ce=(ae[0],ae[1],Object(c.useState)("")),se=Object(i.a)(ce,2),ne=(se[0],se[1],Object(c.useState)("")),re=Object(i.a)(ne,2),je=re[0],be=re[1],oe=function(){var e=Object(o.a)(b.a.mark((function e(){var t;return b.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,t={name:L,username:F,ACL:P,email:z,phone:G},e.next=4,fetch("http://localhost:8000/api_v1/main/users/take_photo/",{method:"post",headers:{"Content-Type":"application/json;charset=utf-8"},body:JSON.stringify(t)});case 4:return e.sent,e.next=7,fetch("http://localhost:8000/api_v1/main/users",{method:"post",headers:{"Content-Type":"application/json;charset=utf-8"},body:JSON.stringify(t)});case 7:e.sent,e.next=13;break;case 10:e.prev=10,e.t0=e.catch(0),console.log("[X]\t Error: userData loading failed:",e.t0);case 13:case"end":return e.stop()}}),e,null,[[0,10]])})));return function(){return e.apply(this,arguments)}}(),ie=function(){var e=Object(o.a)(b.a.mark((function e(){var t,c;return b.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,S(!0),e.next=4,fetch("http://localhost:8000/api_v1/main/users/login/",{method:"GET",headers:{"Content-Type":"application/json;charset=utf-8"}});case 4:return t=e.sent,e.next=7,t.json();case 7:(c=e.sent).status&&(a(c.status),c.data&&(be(c.data),p(c.data.photo_url),m(c.data.photo_url))),e.next=14;break;case 11:e.prev=11,e.t0=e.catch(0),console.log("[X]\t Error: login failed:",e.t0);case 14:case"end":return e.stop()}}),e,null,[[0,11]])})));return function(){return e.apply(this,arguments)}}();return Object(u.jsx)("div",{className:"App",children:Object(u.jsxs)("header",{className:"App-header",children:[Object(u.jsx)("div",{className:"App-topbar",children:Object(u.jsx)("button",{className:"App-topbar-btn",onClick:function(){A(!0)},children:"Admin panel"})}),Object(u.jsxs)("div",{style:{flexDirection:"row"},children:[!v&&Object(u.jsx)("img",{src:l,className:"App-logo",alt:"logo"}),v&&Object(u.jsxs)("div",{style:{flexDirection:"row"},children:[Object(u.jsx)("img",{src:O,className:"App-logo",alt:"image1"}),Object(u.jsx)("img",{src:d,className:"App-logo",alt:"image2"})]}),Object(u.jsx)("p",{children:"Biometric Face Recognition"}),Object(u.jsx)("button",{className:"Login-button",onClick:ie,children:"Login"})]}),Object(u.jsxs)("p",{className:"App-result-area",children:["Response:",Object(u.jsx)("br",{}),je]}),N&&Object(u.jsxs)("form",{onSubmit:oe,children:[Object(u.jsxs)("label",{children:["Name:",Object(u.jsx)("input",{type:"text",value:L,onChange:T})]}),Object(u.jsx)("br",{}),Object(u.jsx)("br",{}),Object(u.jsxs)("label",{children:["Username:",Object(u.jsx)("input",{type:"text",value:L,onChange:D})]}),Object(u.jsx)("br",{}),Object(u.jsx)("br",{}),Object(u.jsxs)("label",{children:["Email:",Object(u.jsx)("input",{type:"text",value:L,onChange:H})]}),Object(u.jsx)("br",{}),Object(u.jsx)("br",{}),Object(u.jsxs)("label",{children:["Phone:",Object(u.jsx)("input",{type:"text",value:L,onChange:M})]}),Object(u.jsx)("br",{}),Object(u.jsx)("br",{}),Object(u.jsxs)("label",{children:["ACL:",Object(u.jsx)("input",{type:"text",value:L,onChange:I})]}),Object(u.jsx)("br",{}),Object(u.jsx)("br",{}),Object(u.jsx)("input",{type:"submit",value:"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c"})]})]})})},p=function(e){e&&e instanceof Function&&a.e(3).then(a.bind(null,16)).then((function(t){var a=t.getCLS,c=t.getFID,s=t.getFCP,n=t.getLCP,r=t.getTTFB;a(e),c(e),s(e),n(e),r(e)}))};r.a.render(Object(u.jsx)(s.a.StrictMode,{children:Object(u.jsx)(O,{})}),document.getElementById("root")),p()}},[[15,1,2]]]);
//# sourceMappingURL=main.66f3fbc4.chunk.js.map