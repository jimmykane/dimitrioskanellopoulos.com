angular.module('app.main').directive('profileIntroduction', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs, $sce, userService, googlePlusService) {
            $scope.profile = googlePlusService.profile || googlePlusService.getProfile(userService.googlePlusUserId);
            $scope.getProfileImageUrl = googlePlusService.getProfileImageUrl;

        },
        link: function(scope, elm, attrs, ctrl) {
        },
        templateUrl: '/assets/app/modules/main/templates/profile.introduction.html'
    }
});