import requests

class CollegeAPI:
    def __init__(self):
        self.api_base_url = 'https://e8b18733-056f-44b7-bc60-3bab61bee43d-00-1lsmyv7ggpj08.picard.replit.dev/'

    def fetch_data(self, endpoint):
        """Função auxiliar para buscar dados da API."""
        try:
            response = requests.get(f"{self.api_base_url}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao buscar dados de {endpoint}: {e}")
            return None

    def get_college_by_id(self, college_id):
        # Fetch data from all relevant endpoints
        college_data = self.fetch_data('')
        courses_data = self.fetch_data('courses')
        exams_data = self.fetch_data('exams')
        information_data = self.fetch_data('information')
        location_data = self.fetch_data('location')
        template_data = self.fetch_data('template')
        date_data = self.fetch_data('date')

        if (college_data is None or courses_data is None or exams_data is None or
        information_data is None or location_data is None or template_data is None or date_data is None):
            return {'error': 'Failed to fetch data from API'}

        # Find the college information
        college = next((item for item in college_data if item['college_id'] == college_id), None)

        if not college:
            return {'error': 'College not found'}

        # Group exams by year
        exams_by_year = {}
        for exam in exams_data:
            year = exam.get('exam_year')
            if year not in exams_by_year:
                exams_by_year[year] = []
            exams_by_year[year].append(exam)

        # Create a combined dictionary with all related information
        result = {
            'college': college,
            'courses': [item for item in courses_data if item['college_id'] == college_id],
            'exams': exams_by_year,
            'information': [item for item in information_data if item['college_id'] == college_id],
            'locations': [item for item in location_data if item['college_id'] == college_id],
            'template': [item for item in template_data if item['college_id'] == college_id],
            'date': [item for item in date_data if item['college_id'] == college_id],
        }

        return result

    def get_all_colleges(self):
        # Fetch data from the main endpoint
        college_data = self.fetch_data('')

        if college_data is None:
            return {'error': 'Failed to fetch data from API'}

        return college_data
    
    def get_all_courses(self):
        course_data = self.fetch_data('courses')

        if course_data is None:
            return {'error': 'Failed to fetch data from API'}

        return course_data
    
    def get_courses_image(self):
        course_image_data = self.fetch_data('course-images')

        if course_image_data is None:
            return {'error': 'Failed to fetch data from API'}

        return course_image_data

    def get_exam_by_id(self, exam_id):
        # Fetch data from the exams endpoint
        exams_data = self.fetch_data('exams')

        if exams_data is None:
            return {'error': 'Failed to fetch data from API'}

        # Find the specific exam information
        exam = next((item for item in exams_data if item['exam_id'] == exam_id), None)

        if not exam:
            return {'error': 'Exam not found'}

        return exam
    
    def get_course_by_id(self, course_id):
        """Busca um curso específico pelo course_id e inclui a imagem correspondente."""
        # Busca todos os cursos
        course_data = self.fetch_data('courses')
        course_image_data = self.fetch_data('course-images')

        if course_data is None or course_image_data is None:
            return {'error': 'Failed to fetch course or image data from API'}

        # Busca o curso específico pelo course_id
        course = next((item for item in course_data if item['course_id'] == course_id), None)

        if not course:
            return {'error': 'Course not found'}

        # Busca a imagem correspondente ao tipo de ciência do curso
        course_image = next((image for image in course_image_data if image['science_type'] == course['science_type']), None)

        if course_image:
            course['course_image_url'] = course_image['course_image_url']
        else:
            course['course_image_url'] = None  # Caso não tenha uma imagem correspondente

        return course
    
    
    def college_for_courses(self, course_id):
        # Busca todos os cursos
        courses_data = self.fetch_data('courses')
        
        if courses_data is None:
            return {'error': 'Failed to fetch courses data from API'}
        
        # Encontra todos os college_id para o course_id específico
        related_college_ids = {course['college_id'] for course in courses_data if course['course_id'] == course_id}

        if not related_college_ids:
            return {'error': 'No related colleges found for this course'}

        # Busca todas as faculdades
        colleges_data = self.fetch_data('')  # Aqui estamos assumindo que a função fetch_data() retornará todas as faculdades

        if colleges_data is None:
            return {'error': 'Failed to fetch colleges data from API'}

        # Filtra as faculdades que possuem os college_id encontrados
        related_colleges = [college for college in colleges_data if college['college_id'] in related_college_ids]

        return related_colleges
