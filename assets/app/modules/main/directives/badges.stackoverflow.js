angular.module('app.main').directive('badgesStackoverflow', function() {
    return {
        restrict: 'A',
        scope: {},
        compile: function(element, attrs) {
        },
        controller: function($scope, $element, $attrs) {
        },
        link: function(scope, elm, attrs, ctrl) {
        },
        template: '<a href="http://stackexchange.com/users/2086410"> <img src="http://stackexchange.com/users/flair/2086410.png" width="208" height="58" alt="profile for Jimmy Kane on Stack Exchange, a network of free, community-driven Q&amp;A sites" title="profile for Jimmy Kane on Stack Exchange, a network of free, community-driven Q&amp;A sites"></a>'
    }
});