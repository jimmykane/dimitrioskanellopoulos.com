angular.module('app.main').directive('project', function() {
    return {
        restrict: 'A', // only activate on element attribute
        scope: true, // New scope to use but rest inherit proto from parent
        compile: function(element, attrs) {
            //player_service.bootstrap();
        },
        controller: function($scope, $element, $attrs) {

        },
        link: function(scope, elm, attrs, ctrl) {

        },
        templateUrl: '/assets/app/modules/main/templates/project.html'
    }
});