from Repository.RepositoryJson import RepositoryJson

from Service.StudentService import StudentService
from Ui.Consola import Consola


def main():
    # testAll()

    studentRepository = RepositoryJson("./student.json")
    problemaLaboratorRepository = RepositoryJson("./problema_laborator.json")
    asignareRepository = RepositoryJson("./asignare.json")

    studentService = StudentService(studentRepository)
    # problemaLaboratorService = ProblemaLaboratorService(problemaLaboratorRepository, asignareRepository)
    # asignareService = AsignareService(asignareRepository, studentRepository, problemaLaboratorRepository)

    studentRepository.loadFromFile()
    problemaLaboratorRepository.loadFromFile()
    asignareRepository.loadFromFile()

    consola = Consola(studentService)
    consola.meniu()

main()
