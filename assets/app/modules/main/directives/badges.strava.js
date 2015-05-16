angular.module('app.main').directive('badgesStrava', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs) {
        },
        link: function(scope, elm, attrs, ctrl) {
        },
        template: '<a style="display:inline-block;background-color:#FC4C02;color:#fff;padding:5px 10px 5px 30px;font-size:11px;font-family:Helvetica, Arial, sans-serif;white-space:nowrap;text-decoration:none;background-repeat:no-repeat;background-position:10px center;border-radius:3px;background-image:url(\'http://badges.strava.com/logo-strava-echelon.png\')" href="http://strava.com/athletes/7586105/badge" target="_clean">Follow me on <img src="http://badges.strava.com/logo-strava.png" alt="Strava" style="margin-left:2px;vertical-align:text-bottom" height=13 width=51 /></a>'
    }
});