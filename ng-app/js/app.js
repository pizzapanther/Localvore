
var localvore = angular.module("localvore", ['ngRoute']);

localvore.config(function ($routeProvider, $locationProvider) {
  $routeProvider
    .when('/', {controller: 'HomePageCtrl', templateUrl: '/tpl/homepage.html'})
    .otherwise({redirectTo: '/'});
    
  $locationProvider.html5Mode(true);
});
