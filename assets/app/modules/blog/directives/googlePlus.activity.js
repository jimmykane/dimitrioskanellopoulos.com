angular.module('app.blog').directive('googlePlusActivity', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs, userService, googlePlusService) {
            $scope.profile = googlePlusService.profile || googlePlusService.getProfile(userService.googlePlusUserId);
        },
        link: function(scope, elm, attrs, ctrl) {
        },
        templateUrl: '/assets/app/modules/main/templates/googlePlus.activity.html'
    }
});