angular.module('app.main').directive('introduction', function(googlePlusService) {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs) {

            var googlePlusUserID = window.googlePlusUserID;

            // The whole profile
            $scope.profile = googlePlusService.profile || googlePlusService.getProfile(googlePlusUserID);

            // About me to be rendered via service
            $scope.getAboutMe = googlePlusService.getAboutMe;

            // Image to be resized via service
            $scope.getProfileImageUrl = googlePlusService.getProfileImageUrl;

        },
        link: function(scope, elm, attrs, ctrl) {

        },
        templateUrl: '/assets/app/modules/main/templates/introduction.html'
    }
});