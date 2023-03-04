from Repository.RepositoryJson import RepositoryJson
from Service.ProblemService import ProblemaLaboratorService
from Service.StudentService import StudentService
from Service.GradeService import AsignareService
from Ui.Consola import Consola


def main():
    # testAll()

    studentRepository = RepositoryJson("./student.json")
    problemaLaboratorRepository = RepositoryJson("./problema_laborator.json")
    asignareRepository = RepositoryJson("./asignare.json")

    studentService = StudentService(studentRepository)
    problemaLaboratorService = ProblemaLaboratorService(problemaLaboratorRepository, asignareRepository)
    asignareService = AsignareService(asignareRepository, studentRepository, problemaLaboratorRepository)

    studentRepository.loadFromFile()
    problemaLaboratorRepository.loadFromFile()
    asignareRepository.loadFromFile()

    consola = Consola(studentService,problemaLaboratorService,asignareService)
    consola.meniu()

main()
