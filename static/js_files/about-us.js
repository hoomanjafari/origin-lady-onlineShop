window.addEventListener('scroll', () => {
    const isDesktop = screen.width >= 1025;
    const isTablet = screen.width >= 768 && screen.width <= 1024;
    const isMobile = screen.width <= 767;

    if (isDesktop) {
        if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
            document.getElementById('about-us-box-2').style.opacity = '100%';
        } else {
            document.getElementById('about-us-box-2').style.opacity = '0';
        };

        if (document.body.scrollTop > 700 || document.documentElement.scrollTop > 700) {
            document.getElementById('about-us-box-3').style.opacity = '100%';
        } else {
            document.getElementById('about-us-box-3').style.opacity = '0';
        }
    } else if (isTablet) {
        if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
            document.getElementById('about-us-box-2').style.opacity = '100%';
        } else {
            document.getElementById('about-us-box-2').style.opacity = '0';
        };

        if (document.body.scrollTop > 700 || document.documentElement.scrollTop > 700) {
            document.getElementById('about-us-box-3').style.opacity = '100%';
        } else {
            document.getElementById('about-us-box-3').style.opacity = '0';
        }
    } else if (isMobile) {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            document.getElementById('about-us-box-2').style.opacity = '100%';
            document.getElementById('about-us-box-3').style.opacity = '100%';
        } else {
            document.getElementById('about-us-box-2').style.opacity = '0';
            document.getElementById('about-us-box-3').style.opacity = '0';
        };

    }
})