angular.module('app.main').directive('personal', function(googlePlusService) {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
            //player_service.bootstrap();
        },
        controller: function($scope, $element, $attrs) {

            var googlePlusUserID = window.googlePlusUserID;

            // The whole profile
            $scope.profile = googlePlusService.profile || googlePlusService.getProfile(googlePlusUserID);

            // About me to be rendered via service
            $scope.getAboutMe = googlePlusService.getAboutMe;

            // Image to be resized via service
            $scope.getProfileImageUrl = googlePlusService.getProfileImageUrl;

            // Check if it's ready (used to show/hide the html)
            $scope.isProfileReady = function (){
                return !angular.equals({}, $scope.profile);
            };

        },
        link: function(scope, elm, attrs, ctrl) {

        },
        templateUrl: '/assets/app/modules/main/templates/personal.html'
    }
});