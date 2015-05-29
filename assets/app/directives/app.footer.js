angular.module('app').directive('footer', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs) {
        },
        link: function(scope, elm, attrs, ctrl) {
        },
        templateUrl: '/assets/app/templates/app.footer.html'
    }
});