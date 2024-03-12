@login_required
@Coordinador_required
def editar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    asignatura_form = AsignaturaForm(instance=asignatura)
    seccion_form = SeccionForm(asignatura_id=asignatura_id)
    
    print("Request method:", request.method)

    if request.method == 'POST':
        print("POST request detected")
        
        if 'guardar_asignatura' in request.POST:
            print("Formulario de asignatura enviado")
            asignatura_form = AsignaturaForm(request.POST, instance=asignatura)
            if asignatura_form.is_valid():
                print("Formulario de asignatura válido")
                asignatura_form.save()
                messages.success(request, "Asignatura modificada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de asignatura inválido")
                print("Errores de validación:", asignatura_form.errors)
        elif 'guardar_seccion' in request.POST:
            print("Formulario de sección enviado")
            seccion_form = SeccionForm(request.POST, asignatura_id=asignatura_id)
            if seccion_form.is_valid():
                print("Formulario de sección válido")
                seccion = seccion_form.save(commit=False)
                seccion.asignatura = asignatura
                seccion.save()
                messages.success(request, "Sección creada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de sección inválido")
                print("Errores de validación:", seccion_form.errors)
    
    return render(request, 'db_coordinador/db_edit_asig.html', {'asignatura_form': asignatura_form, 'seccion_form': seccion_form, 'asignatura': asignatura})



---v2



@login_required
@Coordinador_required
def editar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    asignatura_form = AsignaturaForm(instance=asignatura)
    seccion_form = SeccionForm(asignatura_id=asignatura_id)
    
    print("Request method:", request.method)

    if request.method == 'POST':
        print("POST request detected")
        
        if 'guardar_asignatura' in request.POST:
            print("Formulario de asignatura enviado")
            asignatura_form = AsignaturaForm(request.POST, instance=asignatura)
            if asignatura_form.is_valid():
                print("Formulario de asignatura válido")
                asignatura_form.save()
                messages.success(request, "Asignatura modificada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de asignatura inválido")
                print("Errores de validación:", asignatura_form.errors)
        elif 'guardar_seccion' in request.POST:
            print("Formulario de sección enviado")
            seccion_form = SeccionForm(request.POST, asignatura_id=asignatura_id)
            if seccion_form.is_valid():
                print("Formulario de sección válido")
                seccion = seccion_form.save(commit=False)
                seccion.asignatura = asignatura
                seccion.save()
                
                # Imprimir los usuarios seleccionados
                print("Usuarios seleccionados:", request.POST.getlist('usuarios'))
                
                # Asignar los usuarios seleccionados al objeto de sección
                seccion.usuarios.set(request.POST.getlist('usuarios'))
                
                messages.success(request, "Sección creada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de sección inválido")
                print("Errores de validación:", seccion_form.errors)
    
    return render(request, 'db_coordinador/db_edit_asig.html', {'asignatura_form': asignatura_form, 'seccion_form': seccion_form, 'asignatura': asignatura})


--- v3


@login_required
@Coordinador_required
def editar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    asignatura_form = AsignaturaForm(instance=asignatura)
    seccion_form = SeccionForm(asignatura_id=asignatura_id)
    
    print("Request method:", request.method)

    secciones = Seccion.objects.filter(asignatura=asignatura)

    if request.method == 'POST':
        print("POST request detected")
        
        if 'guardar_asignatura' in request.POST:
            print("Formulario de asignatura enviado")
            asignatura_form = AsignaturaForm(request.POST, instance=asignatura)
            if asignatura_form.is_valid():
                print("Formulario de asignatura válido")
                asignatura_form.save()
                messages.success(request, "Asignatura modificada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de asignatura inválido")
                print("Errores de validación:", asignatura_form.errors)
        elif 'guardar_seccion' in request.POST:
            print("Formulario de sección enviado")
            seccion_form = SeccionForm(request.POST, asignatura_id=asignatura_id)
            if seccion_form.is_valid():
                print("Formulario de sección válido")
                seccion = seccion_form.save(commit=False)
                seccion.asignatura = asignatura
                seccion.save()
                
                # Imprimir los usuarios seleccionados
                print("Usuarios seleccionados:", request.POST.getlist('usuarios'))
                
                # Asignar los usuarios seleccionados al objeto de sección
                seccion.usuarios.set(request.POST.getlist('usuarios'))
                
                messages.success(request, "Sección creada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de sección inválido")
                print("Errores de validación:", seccion_form.errors)
        

        elif 'eliminar_seccion' in request.POST:
            seccion_id = request.POST.get('eliminar_seccion')
            try:
                seccion = Seccion.objects.get(id=seccion_id, asignatura=asignatura)
                seccion.delete()
                messages.success(request, "Sección eliminada correctamente!")
            except Seccion.DoesNotExist:
                 messages.error(request, "La sección que intentas eliminar no existe o no está asociada a esta asignatura.")
            return redirect(reverse('editar_asignatura', kwargs={'asignatura_id': asignatura_id}))
    
    return render(request, 'db_coordinador/db_edit_asig.html', {'asignatura_form': asignatura_form, 'seccion_form': seccion_form, 'asignatura': asignatura,'secciones': secciones})


---ZeroDivisionError


@login_required
@Coordinador_required
def editar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    asignatura_form = AsignaturaForm(instance=asignatura)
    seccion_form = SeccionForm(asignatura_id=asignatura_id)
    
    print("Request method:", request.method)

    secciones = Seccion.objects.filter(asignatura=asignatura)


    if request.method == 'POST':
        print("POST request detected")
        
        if 'guardar_asignatura' in request.POST:
            print("Formulario de asignatura enviado")
            asignatura_form = AsignaturaForm(request.POST, instance=asignatura)
            if asignatura_form.is_valid():
                print("Formulario de asignatura válido")
                asignatura_form.save()
                messages.success(request, "Asignatura modificada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de asignatura inválido")
                print("Errores de validación:", asignatura_form.errors)
        elif 'guardar_seccion' in request.POST:
            print("Formulario de sección enviado")
            seccion_form = SeccionForm(request.POST, asignatura_id=asignatura_id)
            if seccion_form.is_valid():
                print("Formulario de sección válido")
                seccion = seccion_form.save(commit=False)
                seccion.asignatura = asignatura
                seccion.save()
                
                # Imprimir los usuarios seleccionados
                print("Usuarios seleccionados:", request.POST.getlist('usuarios'))
                
                # Asignar los usuarios seleccionados al objeto de sección
                seccion.usuarios.set(request.POST.getlist('usuarios'))
                
                messages.success(request, "Sección creada correctamente!")
                return redirect('gest_asig')
            else:
                print("Formulario de sección inválido")
                print("Errores de validación:", seccion_form.errors)
        

        elif 'eliminar_seccion' in request.POST:
            seccion_id = request.POST.get('eliminar_seccion')
            try:
                seccion = Seccion.objects.get(id=seccion_id, asignatura=asignatura)
                seccion.delete()
                messages.success(request, "Sección eliminada correctamente!")
            except Seccion.DoesNotExist:
                 messages.error(request, "La sección que intentas eliminar no existe o no está asociada a esta asignatura.")
            return redirect(reverse('editar_asignatura', kwargs={'asignatura_id': asignatura_id}))
        
        elif 'editar_seccion' in request.POST:
            seccion_id = request.POST.get('editar_seccion_id')
            seccion_nombre_id = request.POST.get('nombre')  # Obtén el ID del nombre de la sección desde el formulario

            try:
                seccion = Seccion.objects.get(id=seccion_id, asignatura=asignatura)
                nombre_seccion = get_object_or_404(NombreSeccion, id=seccion_nombre_id)  # Recupera la instancia de NombreSeccion
                seccion.nombre = nombre_seccion  # Asigna la instancia de NombreSeccion al campo nombre

                seccion.save()  # Intenta guardar la instancia de Seccion
                messages.success(request, "Sección editada correctamente")
            except Seccion.DoesNotExist:
                messages.error(request, "La sección que intentas editar no existe o no está asociada a esta asignatura.")
            except NombreSeccion.DoesNotExist:
                messages.error(request, "El nombre de la sección proporcionado no es válido.")

            return redirect(reverse('editar_asignatura', kwargs={'asignatura_id': asignatura_id}))

    
    return render(request, 'db_coordinador/db_edit_asig.html', {'asignatura_form': asignatura_form, 'seccion_form': seccion_form, 'asignatura': asignatura,'secciones': secciones})