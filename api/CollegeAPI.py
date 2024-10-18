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

if __name__ == "__main__":
    api = CollegeAPI()
    college_id = 101  # Example college ID

    # Get information for a specific college
    print("Getting information for college ID:", college_id)
    college_info = api.get_college_by_id(college_id)
    print(college_info)

    # Get all colleges
    print("\nGetting all colleges")
    all_colleges = api.get_all_colleges()
    print(all_colleges)

    # Example exam ID
    exam_id = 401
    print(f"\nGetting exam details for exam ID: {exam_id}")
    exam_info = api.get_exam_by_id(exam_id)
    print(exam_info)
