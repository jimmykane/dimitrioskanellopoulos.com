angular.module('app.main').directive('introduction', function(googlePlusService) {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $sce, $element, $attrs) {

            var googlePlusUserID = window.googlePlusUserId;

            // The whole profile
            $scope.profile = googlePlusService.profile || googlePlusService.getProfile(googlePlusUserId);

            // About me to be rendered via service
            $scope.getAboutMe = function (){
                return $sce.trustAsHtml($scope.profile.aboutMe);
            };

            // Image to be resized via service
            $scope.getProfileImageUrl = googlePlusService.getProfileImageUrl;

        },
        link: function(scope, elm, attrs, ctrl) {

        },
        templateUrl: '/assets/app/modules/main/templates/introduction.html'
    }
});