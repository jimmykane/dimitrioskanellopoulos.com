angular.module('app.main').directive('badgesGooglePlus', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
            // Add the js dynamically and let them render
            var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
            po.src = 'https://apis.google.com/js/platform.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
        },
        controller: function($scope, $element, $attrs) {
        },
        link: function(scope, elm, attrs, ctrl) {
        },
        template: '<div class="g-person" data-width="273" data-href="//plus.google.com/u/0/102445631084043565507" data-layout="landscape" data-rel="author"></div>'
    }
});