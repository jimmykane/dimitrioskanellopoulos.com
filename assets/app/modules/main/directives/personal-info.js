angular.module('app.main').directive('personalInfo', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
            //player_service.bootstrap();
        },
        controller: function($scope, $element, $attrs, userService, googlePlusService) {
            $scope.profile = googlePlusService.profile || googlePlusService.getProfile(userService.googlePlusUserId);
        },
        link: function(scope, elm, attrs, ctrl) {
        },
        templateUrl: '/assets/app/modules/main/templates/personal-info.html'
    }
});