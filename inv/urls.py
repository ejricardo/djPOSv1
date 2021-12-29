from django.urls import path
from.views import CategoriaView, CategoriaNew, CategoriaEdit,CategoriaDelete,CategoriaDel, \
    SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, \
    MarcaView, MarcaNew, MarcaEdit, MarcaDel, marca_inactivar, \
    UnidadMedidaView, UnidadMedidaNew, UnidadMedidaEdit, unidadmedida_inactivar, \
    ProductoView, ProductoNew, ProductoEdit, producto_inactivar

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDelete.as_view(), name='categoria_delete'),
    path('categorias/del/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),

    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/del/<int:pk>', SubCategoriaDel.as_view(), name='subcategoria_del'),

    path('marcas/', MarcaView.as_view(), name='marca_list'),
    path('marcas/new', MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactivar/<int:id>', marca_inactivar, name='marca_inactivar'),

    path('unidadmedida/', UnidadMedidaView.as_view(), name='unidadmedida_list'),
    path('unidadmedida/new', UnidadMedidaNew.as_view(), name='unidadmedida_new'),
    path('unidadmedida/edit/<int:pk>', UnidadMedidaEdit.as_view(), name='unidadmedida_edit'),
    path('unidadmedida/inactivar/<int:id>', unidadmedida_inactivar, name='unidadmedida_inactivar'),

    path('productos/', ProductoView.as_view(), name='producto_list'),
    path('productos/new', ProductoNew.as_view(), name='producto_new'),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path('productos/inactivar/<int:id>', producto_inactivar, name='producto_inactivar'),
]