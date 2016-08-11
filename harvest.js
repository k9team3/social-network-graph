friends = [];
var raws = document.getElementsByTagName("a");
for (i = 0; i < raws.length; i++) {
    if (raws[i].href.indexOf("?fref=pb&hc_location=friends_tab") != -1) {
        if (raws[i].innerHTML.indexOf("<img") == -1) {
            friends.push(raws[i].innerHTML);
        }
    }
}
u = friends.filter(function(item, pos) {
    return friends.indexOf(item) == pos;
});
clear();
for (i = 0; i < u.length; i++) {
    console.log(u[i] + ",");
}