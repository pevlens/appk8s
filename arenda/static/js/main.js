document.addEventListener('DOMContentLoaded', function () {
    const mainCategoryItems = document.querySelectorAll('.main-category-item');

    mainCategoryItems.forEach((item) => {
        item.addEventListener('mouseenter', () => {
            const subcategories = item.querySelector('.subcategories');
            if (subcategories) {
                subcategories.style.display = 'block';
            }
        });

        item.addEventListener('mouseleave', () => {
            const subcategories = item.querySelector('.subcategories');
            if (subcategories) {
                subcategories.style.display = 'none';
            }
        });
    });
});