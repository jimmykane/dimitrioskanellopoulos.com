angular.module('app.main').directive('fitnessInfo', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs, userService, fitnessService) {
            // Weight
            $scope.weightMeasurements = fitnessService.getWeightMeasurements(userService.runkeeperUserId);
            // Latest Activity
            $scope.latestActivity = fitnessService.getLatestActivity(userService.runkeeperUserId);
            // Activities Records
            $scope.records = fitnessService.getActivityRecords(userService.runkeeperUserId);
            // @todo Should it just check one?
            $scope.isFitnessDataReady = function () {
                return !angular.equals({}, $scope.weightMeasurements) && !angular.equals({}, $scope.getLatestActivity) && !angular.equals({}, $scope.getLatestActivity);
            };
        },
        link: function(scope, elm, attrs, ctrl) {
        },
        templateUrl: '/assets/app/modules/main/templates/fitness.html'
    }
});