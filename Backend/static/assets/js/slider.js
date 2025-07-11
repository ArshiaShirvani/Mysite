$(document).ready(function () {
    $('.slider').slick({
        slidesToShow: 3, // تعداد کارت‌ها در دسکتاپ
        slidesToScroll: 1, // یک کارت در هر اسکرول
        autoplay: true,
        autoplaySpeed: 1500,
        prevArrow: '<button class="slick-prev"><i class="fa-solid fa-arrow-left"></i></button>',
        nextArrow: '<button class="slick-next"><i class="fa-solid fa-arrow-right"></i></button>',
        responsive: [
            {
                breakpoint: 1024,
                settings: { slidesToShow: 2 } // دو کارت در تبلت
            },
            {
                breakpoint: 600,
                settings: { slidesToShow: 1 } // یک کارت در موبایل
            }
        ]
    });
  
    // اطمینان از نمایش دکمه‌ها در هنگام hover بر روی اسلایدر
    $('.slider').hover(
        function () {
            $('.slick-prev, .slick-next').css('opacity', '1');
        },
        function () {
            $('.slick-prev, .slick-next').css('opacity', '0');
        }
    );
  });
  