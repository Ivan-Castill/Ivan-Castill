Module Module1
    Sub Main()
        ' Generar y mostrar las tablas de división del 1 al 10
        For i As Integer = 1 To 10
            For j As Integer = 1 To 10
                Dim resultado As Double = i / j
                Console.Write(resultado.ToString("0.00").PadLeft(7))
            Next
            Console.WriteLine()
        Next
        Console.ReadLine()
    End Sub
End Module
