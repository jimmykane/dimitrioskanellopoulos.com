angular.module('app.main').directive('brainInfo', function(googlePlusService) {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs) {

            var googlePlusUserID = window.googlePlusUserID;

            // The whole profile
            $scope.profile = googlePlusService.profile || googlePlusService.getProfile(googlePlusUserID);

        },
        link: function(scope, elm, attrs, ctrl) {

        },
        templateUrl: '/assets/app/modules/main/templates/brain.html'
    }
});