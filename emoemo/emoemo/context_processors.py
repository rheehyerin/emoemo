
def themes(request):
    return {
        'themes': {
            'background_colors': ['#FE4365', '#FC9D9A', '#F9CDAD', '#C8C8A9', '#83AF9B', '#8C2318', '#F2C45A'],
            'fonts': ['font1', 'font2', 'font3'],
        },
    }
