angular.module('app.main').directive('introductionMy', function() {
    return {
        restrict: 'E', // only activate on element attribute
        scope: true, // New scope to use but rest inherit proto from parent
        compile: function(element, attrs) {
            //player_service.bootstrap();
            console.log(1);
        },
        controller: function($scope, $element, $attrs) {
                        console.log(2);


        },
        link: function(scope, elm, attrs, ctrl) {
                        console.log(3);

        },
        templateUrl: '../templates/introduction.html'
    }
});