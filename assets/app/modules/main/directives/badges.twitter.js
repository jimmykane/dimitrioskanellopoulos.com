angular.module('app.main').directive('badgesTwitter', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
            !function(d,s,id){
                var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';
                if(!d.getElementById(id)){
                    js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);
                }
            }(document,"script","twitter-wjs");
        },
        controller: function($scope, $element, $attrs) {
        },
        link: function(scope, elm, attrs, ctrl) {
        },
        template: '<a height="100" width="100" class="twitter-timeline" href="https://twitter.com/JimmyKane9" data-widget-id="599636785124253696">Tweets by @JimmyKane9</a>'
    }
});