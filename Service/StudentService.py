from Domain.Student import Student
from Domain.dto import StudentNotaAssembler
from Repository.Repository import Repository
from Repository.RepoInMemory import RepositoryInMemory
from Repository.RepositoryJson import RepositoryJson

class StudentService:
    def __init__(self, studentRepository: RepositoryJson):
        self.__sudentRepository = studentRepository

    def getAllStudenti(self):
        '''
        returneaza lista de studenti
        :return: o lista de obiecte de tipul Student
        '''
        return self.__sudentRepository.getAll()

    def adaugaStudent(self, idStudent, nume, nrPrezente,nota):
        '''
        adauga un student
        :param idStudent:   string
        :param nume:    string
        :param grup:    string
        :return:
        '''
        ok=0;
        for student in self.getAllStudenti():
            if student.getIdEntity()==idStudent:
                ok=1
        if ok==1:
            print("ID-ul exista deja")
        else:
            student = Student(idStudent, nume,nrPrezente,nota)
            self.__sudentRepository.adauga(student)

    def stergeStudent(self, idStudent):
        '''
        sterge un student care are id-ul idStudent
        :param idStudent: string
        :return:
        '''
        # asignari = self.__asignareRepository.getAll()
        # for asignare in asignari:
        #     if asignare.getIdStudent() == idStudent:
        #         self.__asignareRepository.sterge(asignare.getIdEntitate())
        self.__sudentRepository.sterge(idStudent)

    def modificaStudent(self, idStudent, numeNou, nrPrezenteNoi,notaNoua):
        '''
        functia modifica toate datele despre un student cu id-ul dat
        :param idStudent: string
        :param numeNou: string
        :param grupNou: string
        :return:
        '''
        studentNou = Student(idStudent, numeNou, nrPrezenteNoi,notaNoua)
        self.__sudentRepository.modifica(studentNou)

    def cautaStudent(self, idStudent):
        '''
        functia cauta si afiseaza studentul cu id-ul dat
        :param idStudent: string
        :return:
        '''
        return self.__sudentRepository.cauta(idStudent)

    def get_student(self, student):
        student_nota = [*self.__sudentRepository.getAll()]
        return list(filter(lambda x: x.getIdEntity() == student.getIdEntity(),  student_nota))

    def ordonare(self, param):
        """

        :param idProblema:
        :param criteriuSortare:
        :return:
        """
        #if self.__problemaRepository.getById(idProblema) is None:
            #raise KeyError("Nu exista o problema cu id-ul dat")
        #asignari = self.__asignareRepository.getAll()
        studenti = self.__sudentRepository.getAll()
        lista = []
        for student in studenti:
            student_asignare = self.get_student(student)
            lista.append(StudentNotaAssembler.createDTO(student, student_asignare))
        if param == 1:
            lista = sorted(lista, key = lambda d: d.nume)
        elif param == 2:
            #return lista.sortDTO()
            lista = sorted(lista, key = lambda d: d.nota)
        else:
            raise KeyError("Sortare inexistenta")
        if lista == []:
            raise ValueError( "Problema cu id-ul introdus nu este asignata niciunui student")

        return lista