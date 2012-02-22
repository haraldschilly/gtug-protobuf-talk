package main

import (
    "log"
    "fmt"
    //"io"
    //"bytes"
    "net"
    "os"
    proto "goprotobuf.googlecode.com/hg/proto"
    "test"
)

func main() {
    m1 := &test.Member{
        Name: proto.String("Linus"),
        Age:  proto.Int32(99),
    }
    m1.Skills = []test.Skill{test.Skill_ASM, test.Skill_C}
    m1_data, err := proto.Marshal(m1)
    if err != nil {
        log.Fatal("marshaling error: ", err)
        os.Exit(1)
    }
    fmt.Println("m1:          ", m1)
    fmt.Println("m1.Skills:   ", m1.Skills)
    fmt.Println("actual data: ", m1_data)
    println("=== unmarshalling m1 into m2 ===")

    m2 := &test.Member{}
    proto.Unmarshal(m1_data, m2)
    fmt.Println("m2:          ", m2)

    port := 9090
    fmt.Println("=== END EXAMPLES / SERVER STARTING at %d ===", port)
    service := fmt.Sprintf(":%d", port)
    tcpAddr, err := net.ResolveTCPAddr("ip4", service)
    checkError(err)

    listener, err := net.ListenTCP("tcp", tcpAddr)
    checkError(err)

    for {
        conn, err := listener.Accept()
        checkError(err)

        input := make([]byte, 1024)
        n, err := conn.Read(input)
        input = input[:n]
        fmt.Println("input: ", input)
        club := &test.Club{}
        err = proto.Unmarshal(input, club)
        checkError(err)

        sum := int32(0)
        fmt.Println("len: ", len(club.Member))
        for _, m := range club.Member {
            sum += *m.Age
        }
        avg := float64(sum) / float64(len(club.Member))
        fmt.Printf("avg age: %f   (sum: %d)\n", avg, sum)
        reply := &test.Reply{Average: proto.Float64(avg)}
        out_data, err := proto.Marshal(reply)
        conn.Write(out_data) // don't care about return value
        conn.Close()         // we're finished with this client
    }

}

func checkError(err os.Error) {
    if err != nil {
        fmt.Fprintf(os.Stderr, "Fatal error: %s", err.String())
        os.Exit(1)
    }
}
