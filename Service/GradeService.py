from Domain.Grade import Asignare
from Domain.exceptii.DuplicateError import DuplicateError
from Domain.dto import StudentNotaAssembler
from Repository.RepositoryJson import RepositoryJson

#from lab78910.domeniu.dto import StudentNotaAssembler


class AsignareService:
    def __init__(self, asignareRepository: RepositoryJson, studentiRepository: RepositoryJson, problemeRepository: RepositoryJson):
        self.__asignareRepository = asignareRepository
        self.__studentiRepository = studentiRepository
        self.__problemaRepository = problemeRepository

    def getAllAsignari(self):
        '''
        returneaza lista de asignari
        :return: o lista de obiecte de tipul Asignare
        '''
        return self.__asignareRepository.getAll()

    def adaugaAsignare(self, idAsignare, idStudent, idProblemaLaborator, nota):
        '''
        adauga o asignare
        :param idAsignare: string
        :param idStudent:   string
        :param idProblemaLaborator:    string
        :param nota:    string
        :return:
        '''
        if self.__studentiRepository.getById(idStudent) is None:
            raise KeyError("Nu exista un student cu id-ul dat")
        if self.__problemaRepository.getById(idProblemaLaborator) is None:
            raise KeyError("Nu exista o problema cu id-ul dat")

        asignari = self.__asignareRepository.getAll()
        for asignare in asignari:
            if asignare.getIdStudent() == idStudent and asignare.getIdProblema() == idProblemaLaborator:
                raise DuplicateError("Studentul este deja inscris la problema data")

        asignare = Asignare(idAsignare, idStudent, idProblemaLaborator, nota)
        self.__asignareRepository.adauga(asignare)

    def stergeAsignare(self, idAsignare):
        '''
        sterge o asignare care are id-ul idStudent si id-ul idProblemaLaborator
        :param idStudent: string
        :param idProblemaLaborator:
        :return:
        '''
        self.__asignareRepository.sterge(idAsignare)

    def modificaAsignare(self, idAsignare, idStudentNou, idProblemaLaboratorNoua, notaNoua):
        '''
        functia modifica toate datele despre o asignare cu id-ul dat
        :param idStudentNou: string
        :param idStudentNou: string
        :param idProblemaLaboratorNoua: string
        :param notaNoua: string
        :return:
        '''
        if self.__studentiRepository.getById(idStudentNou) is None:
            raise KeyError("Nu exista un student cu id-ul dat")
        if self.__problemaRepository.getById(idProblemaLaboratorNoua) is None:
            raise KeyError("Nu exista o problema cu id-ul dat")

        asignareNoua = Asignare(idAsignare, idStudentNou, idProblemaLaboratorNoua, notaNoua)
        self.__asignareRepository.modifica(asignareNoua)

    def cautareAsignare(self, idAsignare):
        '''
        functia cauta si afiseaza asignarea cu id-ul dat
        :param idAsignare: string
        :return:
        '''
        return self.__asignareRepository.cauta(idAsignare)

    def get_student(self, student):
        student_nota = [*self.__asignareRepository.getAll()]
        return list(filter(lambda x: x.getIdStudent() == student.getIdEntity(),  student_nota))

    def ordonare(self, param):
        """

        :param idProblema:
        :param criteriuSortare:
        :return:
        """
        #if self.__problemaRepository.getById(idProblema) is None:
            #raise KeyError("Nu exista o problema cu id-ul dat")
        #asignari = self.__asignareRepository.getAll()
        studenti = self.__studentiRepository.getAll()
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


    def getStudentiCuMedieSubCinci(self):
        '''listaNote = []
        listaAsign = self.getAllAsignari()
        listaStud = self.__studentiRepository.getAll()
        for student in listaStud:
            nrNote = 0
            sumNote = 0
            for asignare in listaAsign:
                if asignare.getIdStudent() == student.getIdEntitate():
                    sumNote = sumNote + int(asignare.getNota())
                    nrNote += 1
            if(nrNote != 0):
                listaNote.append(sumNote/nrNote)
        rez = []
        i = 0
        for student in listaStud:
            j = 0
            for nota in listaNote:
                if i == j:
                    if(nota < 5):
                        rez.append((student.getNume(),nota))
                    break
                j += 1
            i += 1
        return rez'''
        lista = []
        lista_nota = [entit.nota for entit in self.ordonare(2)]
        for nota in lista_nota:
            for note in nota:
                if float(note) <= 5 and float(note) != None:
                    lista.append(float(note))
        return lista