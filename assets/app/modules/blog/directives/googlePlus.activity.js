angular.module('app.blog').directive('googlePlusActivity', function() {
    return {
        restrict: 'A',
        scope: {
            googlePlusActivity: '='
        },
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs, $sce) {
            $scope.googlePlusActivity.getContent = function (){
                return $sce.trustAsHtml($scope.googlePlusActivity.object.content);
            };
        },
        link: function(scope, elm, attrs, ctrl) {
        },
        templateUrl: '/assets/app/modules/blog/templates/googlePlus.activity.html'
    }
});