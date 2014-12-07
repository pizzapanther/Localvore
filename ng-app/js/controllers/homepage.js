
localvore.controller("HomePageCtrl", function ($scope, $http) {
  $scope.set_title('The small business guide for the local consumer', true);
  
  $scope.cats = [
    {slug: 'farmers-markets', name: 'Farmers Markets'},
    {slug: 'restaurants', name: 'Restuarants'},
    {slug: 'stores', name: 'Stores'}
  ];
  
  $scope.get_featured = function () {
    
    var url = '/backend/api/featured.json';
    $http.get(url)
    .success(function (data) {
      $scope.cats[0].featured = data['farmers-markets'];
      $scope.cats[1].featured = data['stores'];
      $scope.cats[2].restuarants = data['restuarants'];
    });
  };
  
  $scope.get_featured();
});
