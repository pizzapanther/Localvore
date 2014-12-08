
localvore.controller("HomePageCtrl", function ($scope, $http) {
  $scope.set_title('The small business guide for the local consumer', true);
  
  $scope.cats = [
    {slug: 'farmers-markets', name: 'Farmers Markets'},
    {slug: 'restaurants', name: 'Restuarants'},
    {slug: 'stores', name: 'Stores'}
  ];
  
  $scope.get_featured = function () {
    var state = $scope.get_pushstate();
    
    if (state) {
      $scope.cats[0].featured = state['farmers-markets'];
      $scope.cats[1].featured = state['stores'];
      $scope.cats[2].restuarants = state['restuarants'];
    }
    
    else {
      var url = '/backend/api/featured.json';
      
      $http.get(url)
      .success(function (data) {
        $scope.cats[0].featured = data['farmers-markets'];
        $scope.cats[1].featured = data['stores'];
        $scope.cats[2].restuarants = data['restuarants'];
        
        $scope.set_pushstate(data);
      });
    }
  };
  
  $scope.get_featured();
});
