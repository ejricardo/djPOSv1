from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required,permission_required
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm
from bases.views import SinPrivilegios


# Create your views here.

class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_categoria"  # controlar accesos en la vista
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'
    # permission_required = "polls.add_choice"


class CategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    # login_url = "base:login"
    success_message = "Categoría creada satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "base:login"
    success_message = "Categoría actualizada satisfactoriamente"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        form.instance.estado = False
        return super().form_valid(form)


class CategoriaDelete(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'

    success_url = reverse_lazy("inv:categoria_list")
    login_url = "base:login"


class SubCategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_subcategoria"  # controlar accesos en la vista
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    # login_url = 'bases:login'


class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)


class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'

    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "base:login"


class MarcaView(SinPrivilegios, generic.ListView):
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    # login_url = 'bases:login'


class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)


class MarcaDel(LoginRequiredMixin, generic.DeleteView):
    model = Marca
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'

    success_url = reverse_lazy("inv:marca_list")
    login_url = "base:login"

@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return redirect("inv:marca_list")

    if request.method == 'GET':
        contexto = {'obj': marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        return redirect("inv:marca_list")

    return render(request, template_name, contexto)


class UnidadMedidaView(SinPrivilegios, generic.ListView):
    model = UnidadMedida
    template_name = "inv/unidadmedida_list.html"
    context_object_name = "obj"
    # login_url = 'bases:login'


class UnidadMedidaNew(LoginRequiredMixin, generic.CreateView):
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'
    context_object_name = 'obj'
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidadmedida_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class UnidadMedidaEdit(LoginRequiredMixin, generic.UpdateView):
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'
    context_object_name = 'obj'
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidadmedida_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)


def unidadmedida_inactivar(request, id):
    unidadmedida = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not unidadmedida:
        return redirect("inv:unidadmedida_list")

    if request.method == 'GET':
        contexto = {'obj': unidadmedida}

    if request.method == 'POST':
        unidadmedida.estado = False
        unidadmedida.save()
        return redirect("inv:unidadmedida_list")

    return render(request, template_name, contexto)


class ProductoView(SinPrivilegios, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)


def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not producto:
        return redirect("inv:producto_list")

    if request.method == 'GET':
        contexto = {'obj': producto}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        messages.success(request, 'Producto inactivado')
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)
