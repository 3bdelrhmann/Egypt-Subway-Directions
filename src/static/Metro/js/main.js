$(document).ready(function () {

  $( function() {
          var availableTags = [
                  'امبابة',
                  'السودان',
                  'الزمالك',
                  'ماسبيرو',
                  'العتبة',
                  'باب الشعرية',
                  'الجيش',
                  'عبده باشا',
                  'العباسية',
                  'المعرض',
                  'استاد القاهرة',
                  'كلية البنات',
                  'الاهرام',
                  'هارون',
                  'هيليوبليس',
                  'الف مسكن',
                  'نادي الشمس',
                  'عين شمس 1',
                  'عين شمس 2',
                  'عمر بن الخطاب',
                  'مطار القاهرة',
                  'المرج الجديدة',
                  'المرج',
                  'عزبة النخل',
                  'محطة عين شمس',
                  'المطرية',
                  'حلمية الزيتون',
                  'حدائق الزيتون',
                  'سراي القبة',
                  'حمامات القبة',
                  'كوبري القبة',
                  'منشية الصدر',
                  'الدمرداش',
                  'غمرة',
                  'عرابي',
                  'ناصر',
                  'سعد زغلول',
                  'السيدة زينب',
                  'الملك الصالح',
                  'مار جرجس',
                  'الزهراء',
                  'دار السلام',
                  'حدائق المعادي',
                  'المعادي',
                  'ثكنات المعادي',
                  'طره البلد',
                  'كوتسيكا',
                  'طره الاسمنت',
                  'المعصرة',
                  'حدائق حلوان',
                  'وادي حوف',
                  'جامعة حلوان',
                  'عين حلوان',
                  'المنيب',
                  'ساقية مكي',
                  'ام المصريين',
                  'الجيزة',
                  'فيصل',
                  'جامعة القاهرة',
                  'البحوث',
                  'الدقي',
                  'الاوبرا',
                  'السادات',
                  'محمد نجيب',
                  'الشهداء',
                  'مسرة',
                  'روض الفرج',
                  'سانتا تريز',
                  'الخلفاوي',
                  'المظلات',
                  'كلية الزراعة',
                  'محطة حلوان',
                  'شبرا الخيمة'        
          ];
          $( "#CurrentStation" ).autocomplete({
            source: availableTags
          });
  
          $( "#DropStation" ).autocomplete({
            source: availableTags
          });
  
          $("#ToggleBtn").click(function(){
            $(".steps").toggle(500);
          } );
  
          $("#GoToDropStation").click(function(){
            var _current_station = document.getElementById('CurrentStation').value
            if(_current_station.length == 0){
              alert('على فكرة انا لازم اعرف المحطة اللي ناوي تركب منها مش رخامة والله');
            }else{
            
            if(availableTags.indexOf(_current_station) > -1 ){
              $(".CurrentStation_Box").hide(250);
              $(".DropStation_Box").show();
              }else{
                $(".ui-helper-hidden-accessible").show().delay(5000).fadeOut();
              }
            }
        });
        } );
  
      
  
  });  
  
  