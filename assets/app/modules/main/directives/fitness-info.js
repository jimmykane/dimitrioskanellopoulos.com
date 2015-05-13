angular.module('app.main').directive('fitnessInfo', function(fitnessService) {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs) {

            var runkeeperUserID = window.runkeeperUserID;

            // Weight
            $scope.weightMeasurements = fitnessService.getWeightMeasurements(runkeeperUserID);

            // Latest Activity
            $scope.latestActivity = fitnessService.getLatestActivity(runkeeperUserID);

            // Activities Records
            $scope.records = fitnessService.getActivityRecords(runkeeperUserID);

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