angular.module('app.main').directive('introduction', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $sce, $element, $attrs, userService, googlePlusService) {
            $scope.profile = googlePlusService.profile || googlePlusService.getProfile(userService.googlePlusUserId);
            $scope.getAboutMe = function (){
                return $sce.trustAsHtml($scope.profile.aboutMe);
            };
            $scope.getProfileImageUrl = googlePlusService.getProfileImageUrl;

        },
        link: function(scope, elm, attrs, ctrl) {
        },
        templateUrl: '/assets/app/modules/main/templates/introduction.html'
    }
});