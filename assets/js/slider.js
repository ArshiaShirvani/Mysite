var swiper = new Swiper('.swiper-container', {
    slidesPerView: 3, // تعداد کارت‌ها در دسکتاپ
    spaceBetween: 20, // فاصله بین کارت‌ها
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    loop: true, // فعال کردن حلقه برای رفتن از آخر به اول و از اول به آخر
    autoplay: {
      delay: 2000, // زمان تاخیر برای اسکرول هر کارت (3000 میلی‌ثانیه = 3 ثانیه)
      disableOnInteraction: false, // اگر کاربر با اسلایدر تعامل داشته باشد، autoplay غیرفعال نمی‌شود
    },
    breakpoints: {
      // برای موبایل تنظیمات را تغییر می‌دهیم
      320: {
        slidesPerView: 1, // یک کارت در موبایل
      },
      769: {
        slidesPerView: 2, // دو کارت در تبلت
      },
      1025: {
        slidesPerView: 3, // سه کارت در دسکتاپ
      }
    },
  });