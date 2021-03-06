


$(document).ready(function() {
    
    function isScrolledIntoView(elem) {
      var docViewTop = $(window).scrollTop();
      var docViewBottom = docViewTop + $(window).height();
  
      var elemTop = $(elem).offset().top;
      var elemBottom = elemTop + $(elem).height();
  
      return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
    }
    
    $(window).scroll(function() {
      $('.scroll-animations .animated').each(function() {
        if (isScrolledIntoView(this) === true) {
          $(this).addClass('animate__animated animate__fadeInLeft');
        }
      });
    });
  
    // Click Animations
    $('button').on('click', function() {
      /*
      If any input is empty make it's border red and shake it. After the animation is complete, remove the shake and animated classes so that the animation can repeat.
      */
      
    
      if ($('#name').val() === '') {
        $('#name').addClass('form-error animate shake').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
          $(this).removeClass('animated shake');
        });
      } else {
        $('#name').removeClass('form-error');
      }
      
      // Check email input
      if ($('#email').val() === '') {
        $('#email').addClass('form-error animated shake').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
          $(this).removeClass('animated shake');
        });
      } else {
        $('#email').removeClass('form-error');
      }
  
      // Check message textarea
      if ($('#message').val() === '') {
        $('#message').addClass('form-error animated shake').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
          $(this).removeClass('animated shake');
        });
      } else {
        $('#message').removeClass('form-error');
      }
  
    });
    
    // Activate hinge effect when h4 is click in last section
    $('.funky-animations h4').on('click', function() {
      $(this).addClass('animate__hinge').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
          $(this).removeClass('animated hinge');
        });
    });
  });
 