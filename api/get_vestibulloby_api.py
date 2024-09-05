import requests

def get_vestibulloby_api_id(faculty_id):
    # Faz a requisição para obter os dados da faculdade
    url_faculty = "https://c3e1bccd-e40f-4642-a5e0-6b45d108af4b-00-3g9s82kxsdncm.picard.replit.dev/"
    response_faculty = requests.get(url_faculty)
    
    if response_faculty.status_code != 200:
        return None, "Erro ao buscar dados da faculdade", 500
    
    faculty_data = response_faculty.json()

    # Filtra a faculdade específica com base no ID
    faculty = next((f for f in faculty_data if f["id_faculdade"] == faculty_id), None)
    
    if faculty is None:
        return None, "Faculdade não encontrada", 404

    # Faz a requisição para obter os dados dos cursos
    url_courses = "https://c3e1bccd-e40f-4642-a5e0-6b45d108af4b-00-3g9s82kxsdncm.picard.replit.dev/courses"
    response_courses = requests.get(url_courses)
    
    if response_courses.status_code != 200:
        return None, "Erro ao buscar dados dos cursos", 500
    
    courses_data = response_courses.json()

    # Filtra os cursos associados à faculdade
    cursos = [course['nome_curso'] for course in courses_data if course['id_faculdade'] == faculty_id]
    
    # Adiciona a lista de cursos ao dicionário da faculdade
    faculty['cursos'] = cursos
    
    return faculty, None, 200  # Retorna a faculdade, uma mensagem de erro (se houver), e o código de status

def get_vestibulloby_api():
    # Faz a requisição para obter os dados da faculdade
    url_faculty = "https://c3e1bccd-e40f-4642-a5e0-6b45d108af4b-00-3g9s82kxsdncm.picard.replit.dev/"
    response_faculty = requests.get(url_faculty)
    
    if response_faculty.status_code != 200:
        return None  # Retorna None se houver um erro
    
    faculty_data = response_faculty.json()
    
    # Faz a requisição para obter os dados dos cursos
    url_courses = "https://c3e1bccd-e40f-4642-a5e0-6b45d108af4b-00-3g9s82kxsdncm.picard.replit.dev/courses"
    response_courses = requests.get(url_courses)
    
    if response_courses.status_code != 200:
        return None  # Retorna None se houver um erro
    
    courses_data = response_courses.json()
    
    # Adiciona os cursos ao dicionário principal
    faculty_api_data = {
        "faculdades": faculty_data,
        "cursos": courses_data
    }
    
    return faculty_api_data  # Retorna o dicionário com faculdades e cursos
